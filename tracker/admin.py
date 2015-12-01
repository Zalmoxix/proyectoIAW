#-*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Cliente, Incidencia


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Cliente)
admin.site.register(Incidencia)

