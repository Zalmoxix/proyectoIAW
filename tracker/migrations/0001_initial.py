# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('homepage', models.URLField()),
                ('cliente_name', models.CharField(default=b'cliente', max_length=200, verbose_name=b'Nombre')),
                ('cliente_descripcion', models.CharField(max_length=200, verbose_name=b'Descripcion')),
                ('cliente_telefono', models.IntegerField(default=0, verbose_name=b'Tel\xc3\xa9fono')),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('incidencia_descripcion', models.CharField(max_length=200, verbose_name=b'Descripcion')),
                ('incidencia_prioridad', models.IntegerField(default=0, verbose_name=b'Prioridad')),
                ('incidencia_fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha creacion')),
                ('incidencia_clases', models.CharField(default=b'Pregunta', max_length=10, choices=[(b'Pregunta', b'Pregunta'), (b'Error', b'Error'), (b'Averia', b'Averia')])),
                ('incidencia_resuelta', models.BooleanField(default=False)),
                ('incidencia_cliente', models.ForeignKey(to='tracker.Cliente')),
            ],
        ),
    ]
