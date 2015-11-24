#-*- encoding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from registration.signals import user_registered

class Cliente(models.Model):
    cliente_name = models.CharField('Nombre', default='cliente', max_length=200)
    cliente_descripcion = models.CharField('Descripcion', max_length=200)
    cliente_telefono = models.IntegerField('Teléfono', default=0)

    def __str__(self):
        return self.cliente_name

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

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('index', kwargs={'pk': self.pk})

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    homepage = models.URLField()


def assure_user_profile_exists(pk):
    """
    Creates a user profile if a User exists, but the
    profile does not exist.  Use this in views or other
    places where you don't have the user object but have the pk.
    """
    user = User.objects.get(pk=pk)
    try:
        # fails if it doesn't exist
        userprofile = user.userprofile
    except UserProfile.DoesNotExist, e:
        userprofile = UserProfile(user=user)
        userprofile.save()
    return


def create_user_profile(**kwargs):
    UserProfile.objects.get_or_create(user=kwargs['user'])

user_registered.connect(create_user_profile)



