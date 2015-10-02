# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20151001_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente_name',
            field=models.CharField(default=b'cliente', max_length=200, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_descripcion',
            field=models.CharField(max_length=200, verbose_name=b'Descripcion'),
        ),
    ]
