from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from .models import Incidencia
from .forms import ClienteForm, IncidenciaForm


class IndexView(generic.ListView):
    template_name = 'registro/index.html'
    context_object_name = 'ultimas_incidencias'

    def get_queryset(self):
        return Incidencia.objects.order_by('-incidencia_fecha')[:5]

class IncidenciaCreate(CreateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    template_name = 'registro/create_form.html'
    success_url = '/'


class IncidenciaUpdate(UpdateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']

class IncidenciaDelete(DeleteView):
    model = Incidencia
    success_url = reverse_lazy('/')
    template_name = 'registro/delconfirm_form.html'

class DetailView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/detail.html'


class ResultsView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/results.html'

