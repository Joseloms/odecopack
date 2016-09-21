# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20160911_1715'),
        ('listasprecios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_dias', models.PositiveIntegerField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Canal')),
            ],
            options={
                'verbose_name_plural': 'Formas de Pago',
            },
        ),
        migrations.AlterUniqueTogether(
            name='diaspago',
            unique_together=set([('canal', 'numero_dias')]),
        ),
    ]
