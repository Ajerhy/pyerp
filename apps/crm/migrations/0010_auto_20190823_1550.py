# Generated by Django 2.2.4 on 2019-08-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20190823_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='pylead',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='pylead',
            name='fc',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pylead',
            name='fm',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='pylead',
            name='uc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pylead',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]