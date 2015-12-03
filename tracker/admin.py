#-*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Cliente, Incidencia

class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = 'cliente'

class UserAdmin(UserAdmin):
    inlines = (ClienteInline, )

admin.site.unregister(User)
admin.site.register(Incidencia)
admin.site.register(User, UserAdmin)

