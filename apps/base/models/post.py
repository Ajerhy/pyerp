# Librerias Standard
import os

# Librerias Django
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

# Librerias de terceros
from apps.base.models import PyFather

# Librerias en carpetas locales
from ..rename_image import RenameImage

_UNSAVED_FILEFIELD = 'unsaved_filefield'


def image_path(instance, filename):
    root, ext = os.path.splitext(filename)
    return "post/{id}{ext}".format(id=instance.pk, ext=ext)


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)

class PyPost(PyFather):
    title = models.CharField('Nombre', max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    keywords = models.CharField('Keywords', max_length=20, blank=True)
    img = models.ImageField(
        max_length=255,
        storage=RenameImage(),
        upload_to=image_path,
        blank=True,
        null=True,
        default='post/default_post.png'
    )

    def get_absolute_url(self):
        return reverse('base:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return format(self.title)


@receiver(pre_save, sender=PyPost)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_FILEFIELD):
        setattr(instance, _UNSAVED_FILEFIELD, instance.img)
        instance.img = 'post/default_post.png'


@receiver(post_save, sender=PyPost)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_FILEFIELD):
        instance.img = getattr(instance, _UNSAVED_FILEFIELD)
        instance.save()
        instance.__dict__.pop(_UNSAVED_FILEFIELD)
    if not instance.img or instance.img is None:
        instance.img = 'post/default_post.png'
        instance.save()
