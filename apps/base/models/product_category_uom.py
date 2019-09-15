# Librerias Django
from django.db import models
from django.urls import reverse

# Librerias en carpetas locales
from .father import PyFather


class PyProductCategoryUOM(PyFather):
    name = models.CharField(max_length=40)

    def __str__(self):
        return format(self.name)

    def get_absolute_url(self):
        return reverse('base:product-category-uom-detail', kwargs={'pk': self.pk})
