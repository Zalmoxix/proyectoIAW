#-*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    url(r'^add/$', views.IncidenciaCreate.as_view(), name='add'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.IncidenciaUpdate.as_view(), name='update'),

    url(r'^(?P<pk>[0-9]+)/delete/$', views.IncidenciaDelete.as_view(), name='delete'),

    url(r'^/profile/detail$', views.UserProfileDetail.as_view(), name='user_profile_detail'),

    url(r'^(?P<pk>[0-9]+)/profile/update/$', views.UserProfileUpdate.as_view(), name='user_profile_edit'),

]


