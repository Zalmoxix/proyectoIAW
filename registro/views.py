from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from .models import Incidencia, Cliente
from .forms import ClienteForm, IncidenciaForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



class IndexView(generic.ListView):
    template_name = 'registro/index.html'
    context_object_name = 'ultimas_incidencias'

    def get_queryset(self):
        return Incidencia.objects.order_by('-incidencia_fecha')[:5]


#@login_required
class IncidenciaCreate(CreateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    template_name = 'registro/create_form.html'
    success_url = '/'

#@login_required
class IncidenciaUpdate(UpdateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    success_url = ('/')

#@login_required
class IncidenciaDelete(DeleteView):
    model = Incidencia
    success_url = ('/')
    template_name = 'registro/delconfirm_form.html'

class DetailView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/detail.html'
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']

class ResultsView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/results.html'

