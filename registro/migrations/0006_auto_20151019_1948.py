# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20151019_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidencia',
            old_name='incidencia_estado',
            new_name='incidencia_resuelta',
        ),
    ]
