# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0005_delete_habitacion'),
        ('proveedores', '0008_auto_20160920_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaPrecio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cantidad_minima', models.DecimalField(decimal_places=3, max_digits=10)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'listas de precios',
            },
        ),
        migrations.CreateModel(
            name='VariableListaPrecio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('referencia', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('value', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Variables Lista Precios',
            },
        ),
        migrations.AlterUniqueTogether(
            name='listaprecio',
            unique_together=set([('proveedor', 'producto', 'cantidad_minima')]),
        ),
    ]
