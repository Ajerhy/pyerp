# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .country import PyCountry
from .father import PyFather

POSITION_CHOICE = (
    ("before", "Antes de la Cantidad"),
    ('after', 'Después de la Cantidad'),
)


class PyCurrency(PyFather):
    name = models.CharField('Nombre', max_length=40)
    alias = models.CharField('Alias', max_length=40)
    symbol = models.CharField('Símbolo', max_length=3)
    country = models.ForeignKey(PyCountry, on_delete=models.PROTECT)
    iso = models.CharField(max_length=30)
    position = models.CharField(
        choices=POSITION_CHOICE, max_length=64, default='after')

    def get_absolute_url(self):
        return reverse('base:currency-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} ({})".format(self.name, self.country)
