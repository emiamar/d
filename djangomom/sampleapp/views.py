import models

from django.db.models.base import ModelBase

import serializer

# imports Generic Views from django_template_project base app
from base.views import (
    SerializerListView,
    SerializerDetailView,
    SerializerCreateView,
    SerializerUpdateView
)

for name, cls in models.__dict__.items():
    if isinstance(cls, ModelBase) and cls._meta.abstract is False:
        view_name = '{0}SerializerListView'.format(name)
        locals()[view_name] = type(
            view_name,
            (SerializerListView,),
            {
                'model': cls,
                'serializer_name': '{0}Serializer'.format(name),
                'serializer': serializer
            }
        )
        view_name = '{0}SerializerDetailView'.format(name)
        locals()[view_name] = type(
            view_name,
            (SerializerDetailView,),
            {
                'model': cls,
                'serializer_name': '{0}Serializer'.format(name),
                'serializer': serializer
            }
        )
        view_name = '{0}SerializerCreateView'.format(name)
        locals()[view_name] = type(
            view_name,
            (SerializerCreateView,),
            {
                'serializer_name': '{0}Serializer'.format(name),
                'serializer': serializer
            }
        )
        view_name = '{0}SerializerUpdateView'.format(name)
        locals()[view_name] = type(
            view_name,
            (SerializerUpdateView,),
            {
                'serializer_name': '{0}Serializer'.format(name),
                'serializer': serializer,
                'model': cls,
            }
        )
