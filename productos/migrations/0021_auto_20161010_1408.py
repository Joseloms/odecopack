# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0020_auto_20161010_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo_base',
            field=models.DecimalField(decimal_places=4, default=0, editable=False, max_digits=10),
        ),
    ]