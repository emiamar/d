"""Djangomon url"""
import views

from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^add_resource/$', views.AddResourceView.as_view(), name='add_resource'),

]
