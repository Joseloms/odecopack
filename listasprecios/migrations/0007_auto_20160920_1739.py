# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listasprecios', '0006_variablelistaprecio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variablelistaprecio',
            name='forma_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listasprecios.FormaPago', unique=True),
        ),
    ]
