#-*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Cliente, Incidencia

admin.site.register(Cliente)
admin.site.register(Incidencia)
