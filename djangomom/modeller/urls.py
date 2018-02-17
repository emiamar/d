from django.conf.urls import url

from .models import *

import views

urlpatterns = [
    # Creates model objs
    url(r'^create/$',
        views.ModelObjectCreateView.as_view(),
        name='create'),
    # Creates model field objs
    url(r'^create_field/$',
        views.ModelFieldCreateView.as_view(),
        name='create_field'),
    # modelobject deatil or list of modelfields for specific modelobject.
    url(r'^detail/(?P<pk>[^/]+)/$',
        views.ModelObjectDetailView.as_view(),
        name='detail'),
    # List of modelobjects for specific app.
    url(r'^(?P<pk>[^/]+)/$',
        views.AppModelObjectListView.as_view(),
        name='index'),
]
