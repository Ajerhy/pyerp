# Generated by Django 2.2.4 on 2019-08-17 21:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_auto_20190817_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pyproduct',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='pyproduct',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created on'),
            preserve_default=False,
        ),
    ]
