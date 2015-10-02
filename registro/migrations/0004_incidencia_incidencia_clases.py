# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20151001_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='incidencia_clases',
            field=models.CharField(default=b'Pregunta', max_length=2, choices=[(b'Pregunta', b'Pregunta'), (b'Error', b'Error'), (b'Averia', b'Averia')]),
        ),
    ]
