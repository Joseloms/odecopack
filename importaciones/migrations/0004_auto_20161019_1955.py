# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importaciones', '0003_auto_20161019_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factorcambiomoneda',
            name='moneda_origen',
        ),
        migrations.DeleteModel(
            name='FactorCambioMoneda',
        ),
    ]
