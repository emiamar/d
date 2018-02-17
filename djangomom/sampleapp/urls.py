from django.conf.urls import url
from django.db.models.base import ModelBase


import views

import models

urlpatterns = [
]


for name, cls in models.__dict__.items():
    if isinstance(cls, ModelBase) and cls._meta.abstract is False:
        view = getattr(views, '{0}SerializerListView'.format(name))
        urlpatterns.append(
            url(r'^{0}_list/$'.format(name.lower()),
                view.as_view(),
                name='{0}_list'.format(name.lower()))
        )
        view = getattr(views, '{0}SerializerDetailView'.format(name))
        urlpatterns.append(
            url(r'^{0}_detail/(?P<pk>[0-9]+)/$'.format(name.lower()),
                view.as_view(),
                name='{0}_detail'.format(name.lower()))
        )
        view = getattr(views, '{0}SerializerUpdateView'.format(name))
        urlpatterns.append(
            url(r'^{0}_update/(?P<pk>[0-9]+)/$'.format(name.lower()),
                view.as_view(),
                name='{0}_update'.format(name.lower()))
        )
        view = getattr(views, '{0}SerializerCreateView'.format(name))
        urlpatterns.append(
            url(r'^{0}_create/$'.format(name.lower()),
                view.as_view(),
                name='{0}_create'.format(name.lower()))
        )
