# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_incidencia_incidencia_clases'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='incidencia_estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='incidencia_clases',
            field=models.CharField(default=b'Pregunta', max_length=10, choices=[(b'Pregunta', b'Pregunta'), (b'Error', b'Error'), (b'Averia', b'Averia')]),
        ),
    ]
