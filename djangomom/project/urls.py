from django.conf.urls import url

from .models import *

import views

urlpatterns = [
    # Project list
    url(r'^$', views.ProjectListView.as_view(),
        name='index'),
    # Create Project
    url(r'^create/$', views.CreateProjectView.as_view(),
        name='create'),
]
