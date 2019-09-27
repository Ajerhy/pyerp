# Librerias Django
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import connections, router, transaction

# Librerias en carpetas locales
from ..models import PySequence
from .web_father import (
    FatherCreateView, FatherDetailView, FatherListView, FatherUpdateView, FatherDeleteView)

from ..models import PySequence

SEQ_FIELDS = [
    {'string': _("Name"), 'field': 'name'},
    {'string': _("Prefix"), 'field': 'prefix'},
    {'string': _("Padding"), 'field': 'padding'},
    {'string': _("Initial"), 'field': 'initial'},
    {'string': _("Increment"), 'field': 'increment'},
    {'string': _("Reset"), 'field': 'reset'},
    {'string': _("Next"), 'field': 'next_seq'},
]

SEQ_SHORT = ['name', 'prefix', 'padding', 'initial', 'increment', 'reset', 'next_seq']


class SequenceListView(FatherListView):
    model = PySequence
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceListView, self).get_context_data(**kwargs)
        context['title'] = 'Sequence'
        context['detail_url'] = 'base:sequence-detail'
        context['add_url'] = 'base:sequence-add'
        context['fields'] = SEQ_FIELDS
        return context


class SequenceDetailView(FatherDetailView):
    model = PySequence
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['update_url'] = 'base:sequence-update'
        context['delete_url'] = 'base:sequence-delete'
        context['fields'] = SEQ_FIELDS
        return context


class SequenceCreateView(FatherCreateView):
    model = PySequence
    fields = SEQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create Sequence'
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['back_url'] = reverse('base:sequences')
        return context


class SequenceUpdateView(FatherUpdateView):
    model = PySequence
    fields = SEQ_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(SequenceUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:sequences', 'name': 'Sequences'}]
        context['back_url'] = reverse('base:sequence-detail', kwargs={'pk': context['object'].pk})
        return context


# ========================================================================== #
class SequenceDeleteView(FatherDeleteView):
    model = PySequence
    success_url = 'base:sequences'


# ========================================================================== #
SELECT = """
    SELECT next_seq
    FROM sequences_sequence
    WHERE name = %s
"""

POSTGRESQL_UPSERT = """
    INSERT INTO sequences_sequence (name, prefix, padding, initial, increment, reset, next_seq)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (name)
    DO UPDATE SET next_seq = sequences_sequence.next_seq + %s
    RETURNING next_seq;
"""

MYSQL_UPSERT = """
    INSERT INTO sequences_sequence (name, prefix, padding, initial, increment, reset, next_seq)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY
    UPDATE next_seq = sequences_sequence.next_seq + %s
"""

def get_next_value(name='default', prefix='default', padding=4, initial=1, increment=1, reset=None, *, nowait=False, using=None):
    """
    Return the next value for a given sequence.
    """
    try:
        sequence = PySequence.objects.get(name=name)
        prefix = sequence.prefix
        initial = sequence.initial
        increment = sequence.increment
        reset = sequence.reset
        padding = sequence.padding
    except PySequence.DoesNotExist:
        sequence = None

    if reset is not None:
        assert initial < reset

    if using is None:
        using = router.db_for_write(PySequence)

    connection = connections[using]

    if (connection.vendor == 'postgresql' and getattr(connection, 'pg_version', 0) >= 90500 and reset is None and not nowait):

        # PostgreSQL ≥ 9.5 supports "upsert".
        # This is about 3x faster as the naive implementation.

        with connection.cursor() as cursor:
            cursor.execute(
                POSTGRESQL_UPSERT,
                [name, prefix, padding, initial, increment, reset, initial]
            )
            result = cursor.fetchone()

        return '{}{}'.format(prefix, str(result[0]).zfill(padding))

    elif (connection.vendor == 'mysql' and reset is None and not nowait):

        # MySQL supports "upsert" but not "returning".
        # This is about 2x faster as the naive implementation.

        with transaction.atomic(using=using, savepoint=False):
            with connection.cursor() as cursor:
                cursor.execute(
                    MYSQL_UPSERT,
                    [name, prefix, padding, initial, increment, reset, initial]
                )
                cursor.execute(SELECT, [name])
                result = cursor.fetchone()
        return '{}{}'.format(prefix, str(result[0]).zfill(padding))

    else:
        # Default, ORM-based implementation for all other cases.
        with transaction.atomic(using=using, savepoint=False):
            sequence, created = (
                PySequence.objects.select_for_update(
                    nowait=nowait
                ).get_or_create(
                    name=name,
                    defaults={
                        'prefix': prefix,
                        'padding': padding,
                        'initial': initial,
                        'increment': increment,
                        'reset': reset,
                        'next_seq': initial
                    }
                )
            )
            if not created:
                if reset is not None and sequence.next_seq >= reset:
                    sequence.next_seq = initial
                sequence.save()
                sequence.next_seq += increment

            return '{}{}'.format(prefix, str(sequence.next_seq).zfill(padding))
