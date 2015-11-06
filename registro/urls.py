from django.conf.urls import url
from . import views
from registro.views import IncidenciaCreate, IncidenciaUpdate, IncidenciaDelete

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    url(r'^add/$', IncidenciaCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/update/$', IncidenciaUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', IncidenciaDelete.as_view(), name='delete'),
]
