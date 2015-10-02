# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente_descripcion', models.CharField(max_length=200)),
                ('cliente_telefono', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('incidencia_descripcion', models.CharField(max_length=200)),
                ('incidencia_prioridad', models.IntegerField(default=0)),
                ('incidencia_cliente', models.ForeignKey(to='registro.Cliente')),
            ],
        ),
    ]
