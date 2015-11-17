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


'''
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
'''


class IndexView(generic.ListView):
    template_name = 'registro/index.html'
    context_object_name = 'ultimas_incidencias'

    def get_queryset(self):
        return Incidencia.objects.order_by('-incidencia_fecha')[:5]
'''
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['contraseña']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))
'''
#@login_required
class IncidenciaCreate(CreateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    template_name = 'registro/create_form.html'
    success_url = '/'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaCreate, self).dispatch(*args, **kwargs)

#@login_required
class IncidenciaUpdate(UpdateView):
    model = Incidencia
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']
    success_url = ('/')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaUpdate, self).dispatch(*args, **kwargs)

#@login_required
class IncidenciaDelete(DeleteView):
    model = Incidencia
    success_url = ('/')
    template_name = 'registro/delconfirm_form.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IncidenciaDelete, self).dispatch(*args, **kwargs)

class DetailView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/detail.html'
    fields = ['incidencia_cliente', 'incidencia_descripcion', 'incidencia_prioridad', 'incidencia_clases']

class ResultsView(generic.DetailView):
    model = Incidencia
    template_name = 'registro/results.html'

