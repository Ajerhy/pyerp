# Librerias Django
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias de terceros
from apps.base.models import PyFather

TYPE = (
        ("indicator", "Indicator"),
        ("table", "Table"),
    )

class PyBi(PyFather):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=255)
    type = models.CharField(_("Type"), null=True, blank=True,  choices=TYPE, max_length=64, default='indicator')
    model = models.CharField(_("Model"), null=True, blank=True,  max_length=50)
    parameter = models.CharField(_("Parameter"), null=True, blank=True, max_length=50)
    color = models.CharField(_("Color"), null=True, blank=True, max_length=50)
    icon = models.CharField(_("Icon"), null=True, blank=True, max_length=50)

    def get_absolute_url(self):
        return reverse('base:bi-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.name)
