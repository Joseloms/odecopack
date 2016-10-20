# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactorCambioMoneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cambio', models.DecimalField(decimal_places=4, max_digits=18)),
            ],
            options={
                'verbose_name_plural': '2. Tasas de Cambio Monedas',
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': '1. Monedas',
            },
        ),
        migrations.AddField(
            model_name='factorcambiomoneda',
            name='moneda_origen',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='moneda_cambio', to='importaciones.Moneda'),
        ),
    ]