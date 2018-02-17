"""Djangomon url"""
import views

from django.conf.urls import url

from .views import *

urlpatterns = [
    # url(r'^$',
    #     'django.contrib.auth.views.login',
    #     {'template_name': 'signin.html'}),
    url(r'^signin/$', views.login_user, name='login_user'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'template_name': 'signin.html'}, name='logout'),
    url(r'^dashboard/$',
        DashboardRedirectView.as_view(), name='dashboard'),
    url(r'^change_password/', views.change_password, name='change_password'),

]
