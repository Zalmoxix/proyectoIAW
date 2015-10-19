#-*- encoding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone



class Cliente(models.Model):
    cliente_name = models.CharField('Nombre', default='cliente', max_length=200)
    cliente_descripcion = models.CharField('Descripcion', max_length=200)
    cliente_telefono = models.IntegerField('Teléfono', default=0)

    def __str__(self):
        return self.cliente_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Incidencia(models.Model):
    incidencia_cliente = models.ForeignKey(Cliente)
    incidencia_descripcion = models.CharField('Descripcion', max_length=200)
    incidencia_prioridad = models.IntegerField('Prioridad', default=0)
    incidencia_fecha = models.DateTimeField('Fecha creacion', auto_now_add=True)
    PREGUNTA='Pregunta'
    ERROR='Error'
    AVERIA='Averia'
    incidencia_clase_tipos = ((PREGUNTA, 'Pregunta'), (ERROR, 'Error'), (AVERIA, 'Averia'), )
    incidencia_clases =models.CharField(max_length=10, choices=incidencia_clase_tipos, default=PREGUNTA)
    incidencia_resuelta = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) #+ '->   ' + self.incidencia_descripcion[:30]

