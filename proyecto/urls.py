#-*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset
import registration

urlpatterns = [
    url(r'^', include('tracker.urls', namespace="tracker")),
    url(r'^tracker/', include('tracker.urls', namespace="tracker")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracker/password/reset/$', password_reset, {'html_email_template_name': 'registration/password_reset_email_html.html'}, name='auth_password_reset',),
    url(r'^tracker/', include('registration.backends.default.urls')),
    url(r'^tracker', include('django.contrib.auth.urls')),

]
