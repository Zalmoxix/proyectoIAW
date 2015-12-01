#-*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Incidencia, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model





class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class IncidenciaForm(ModelForm):
    class Meta:
        model = Incidencia
        fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegistrationFormMod(RegistrationForm):



    email = forms.EmailField(label=("E-mail"))

    class Meta:
        model = Cliente
        fields = ('email',)
