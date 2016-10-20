# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('importaciones', '0001_initial'),
        ('productos_categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MargenProvedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('margen_deseado', models.DecimalField(decimal_places=3, max_digits=18, verbose_name='Margen (%)')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_margenes_por_proveedor', to='productos_categorias.CategoriaProducto')),
            ],
            options={
                'verbose_name_plural': '2. Margenes x Categoría x Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('factor_importacion', models.DecimalField(decimal_places=3, default=1, max_digits=18)),
                ('margenes', models.ManyToManyField(through='proveedores.MargenProvedor', to='productos_categorias.CategoriaProducto')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='provedores_con_moneda', to='importaciones.Moneda')),
            ],
            options={
                'verbose_name_plural': '1. Proveedores',
            },
        ),
        migrations.AddField(
            model_name='margenprovedor',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_margenes_por_categoria', to='proveedores.Proveedor'),
        ),
        migrations.AlterUniqueTogether(
            name='margenprovedor',
            unique_together=set([('categoria', 'proveedor')]),
        ),
    ]
