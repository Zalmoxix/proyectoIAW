# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='incidencia_fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 19, 26, 8, 458000, tzinfo=utc), verbose_name=b'Fecha creacion', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_descripcion',
            field=models.CharField(max_length=200, verbose_name=b'Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_telefono',
            field=models.IntegerField(default=0, verbose_name=b'Tel\xc3\xa9fono'),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='incidencia_descripcion',
            field=models.CharField(max_length=200, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='incidencia_prioridad',
            field=models.IntegerField(default=0, verbose_name=b'Prioridad'),
        ),
    ]
