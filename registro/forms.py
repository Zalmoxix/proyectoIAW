from django import forms
from django.forms import ModelForm
from .models import Incidencia, Cliente


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class IncidenciaForm(ModelForm):
    class Meta:
        model = Incidencia
        fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
