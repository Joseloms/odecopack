# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0022_auto_20161007_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banda',
            old_name='empujador',
            new_name='con_aleta',
        ),
        migrations.AddField(
            model_name='banda',
            name='con_empujador',
            field=models.BooleanField(default=False),
        ),
    ]