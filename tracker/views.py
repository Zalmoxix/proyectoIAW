#-*- encoding: utf-8 -*-
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
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'ultimas_incidencias'

    def get_queryset(self):
        return Incidencia.objects.order_by('-incidencia_fecha')[:10]

class IncidenciaCreate(CreateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    template_name = 'tracker/create_form.html'
    success_url = '/'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaCreate, self).dispatch(*args, **kwargs)

class IncidenciaUpdate(UpdateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    success_url = ('/')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaUpdate, self).dispatch(*args, **kwargs)

class IncidenciaDelete(DeleteView):
    model = Incidencia
    success_url = ('/')
    template_name = 'tracker/delconfirm_form.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaDelete, self).dispatch(*args, **kwargs)

class DetailView(generic.DetailView):
    model = Incidencia
    template_name = 'tracker/detail.html'
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']

class ResultsView(generic.DetailView):
    model = Incidencia
    template_name = 'tracker/results.html'

class UserProfileDetail(DetailView):
    model = Cliente
    template_name = 'user/userprofile_detail.html'
    def get_object(self, queryset=None):
        return self.request.user
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserProfileDetail, self).dispatch(*args, **kwargs)


class UserProfileUpdate(UpdateView):
    model = Cliente
    fields = ('homepage',)
    template_name = 'user/userprofile_form.html'

    def get(self, request, *args, **kwargs):
        assure_user_profile_exists(kwargs['pk'])
        return (super(UserProfileUpdate, self).
                get(self, request, *args, **kwargs))

