# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 19:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBiable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vende_nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('vende_id', models.PositiveIntegerField(blank=True, null=True)),
                ('tipo_docu_id', models.CharField(blank=True, max_length=10, null=True)),
                ('cli_nit', models.CharField(blank=True, max_length=16, null=True)),
                ('item_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('tipo_doc_descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('proyecto_id', models.CharField(blank=True, max_length=50, null=True)),
                ('documento_fc', models.CharField(blank=True, max_length=50, null=True)),
                ('cli_raz_social', models.CharField(blank=True, max_length=120, null=True)),
                ('item_id', models.PositiveIntegerField(blank=True, null=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now)),
                ('tipo_documento_relacionado', models.CharField(blank=True, max_length=10, null=True)),
                ('nro_documento_relacionado', models.PositiveIntegerField(blank=True, null=True)),
                ('tipo_rm_relacionado', models.CharField(blank=True, max_length=10, null=True)),
                ('nro_rm_relacionado', models.PositiveIntegerField(blank=True, null=True)),
                ('valor_bruto', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('descuentos_netos', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('impuestos_netos', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('valor_neto', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('costo', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('rentabilidad', models.DecimalField(decimal_places=4, default=0, max_digits=14)),
                ('fecha_generacion_biable', models.DateField(default=datetime.datetime.now)),
                ('numero_registros', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
