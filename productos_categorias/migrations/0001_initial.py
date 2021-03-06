# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('nomenclatura', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'verbose_name_plural': '2. Categorías 2',
                'verbose_name': '2. Categoría 2',
            },
        ),
        migrations.CreateModel(
            name='CategoriaDosCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_dos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_categorias_uno', to='productos_categorias.CategoriaDos', verbose_name='categoría dos')),
            ],
            options={
                'verbose_name_plural': '5. Categorías 2 Productos',
                'verbose_name': '5. Categoría 2 Producto',
            },
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('nomenclatura', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'verbose_name_plural': '3. Categorías 1',
                'verbose_name': '3. Categoría 1',
            },
        ),
        migrations.CreateModel(
            name='ProductoNombreConfiguracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_categoría_uno', models.BooleanField(default=False)),
                ('con_categoría_dos', models.BooleanField(default=False)),
                ('con_serie', models.BooleanField(default=False)),
                ('con_fabricante', models.BooleanField(default=False)),
                ('con_tipo', models.BooleanField(default=False)),
                ('con_material', models.BooleanField(default=False)),
                ('con_color', models.BooleanField(default=False)),
                ('con_ancho', models.BooleanField(default=False)),
                ('con_alto', models.BooleanField(default=False)),
                ('con_longitud', models.BooleanField(default=False)),
                ('con_diametro', models.BooleanField(default=False)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mi_configuracion_producto_nombre_estandar', to='productos_categorias.CategoriaProducto', verbose_name='categoría')),
            ],
            options={
                'verbose_name_plural': 'Configuración Nombre Automático',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('nomenclatura', models.CharField(max_length=4, unique=True)),
            ],
            options={
                'verbose_name_plural': '1. Tipo Producto',
                'verbose_name': '1. Tipos Productos',
            },
        ),
        migrations.CreateModel(
            name='TipoProductoCategoría',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_uno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_tipo', to='productos_categorias.CategoriaProducto', verbose_name='categorías uno')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_categorias', to='productos_categorias.TipoProducto', verbose_name='tipo')),
            ],
            options={
                'verbose_name_plural': '3. Tipo por Categoria',
                'verbose_name': '3. Tipos por Categoria',
            },
        ),
        migrations.AddField(
            model_name='categoriadoscategoria',
            name='categoria_uno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_categorias_dos', to='productos_categorias.CategoriaProducto', verbose_name='categoría uno'),
        ),
        migrations.AlterUniqueTogether(
            name='tipoproductocategoría',
            unique_together=set([('categoria_uno', 'tipo')]),
        ),
        migrations.AlterUniqueTogether(
            name='categoriadoscategoria',
            unique_together=set([('categoria_uno', 'categoria_dos')]),
        ),
    ]
