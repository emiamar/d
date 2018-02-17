"""Djangomon url"""
import views

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^signin/$', views.login_user, name='login_user'),
    url(r'^$', views.login_user, name='home'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'template_name': 'signin.html'}, name='logout'),
    url(r'^dashboard/$',
        DashboardRedirectView.as_view(), name='dashboard'),
    url(r'^change_password/', views.change_password, name='change_password'),

]
