# Generated by Django 2.2.4 on 2019-08-17 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytask',
            name='income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ingreso'),
        ),
        migrations.AddField(
            model_name='pytask',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
