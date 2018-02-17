from django.db.models.base import ModelBase

import models

from rest_framework import serializers

from .helper import classify


for name, cls in models.__dict__.items():
    if isinstance(cls, ModelBase) and cls._meta.abstract is False:
        Meta = type(
            'Meta',
            (object,),
            {
                'model': cls,
                'fields': '__all__'
            }
        )
        serializer_name = '{0}Serializer'.format(name)
        globals()[serializer_name] = type(
            serializer_name,
            (serializers.ModelSerializer,),
            {
                'Meta': Meta,
            }
        )

for name, cls in models.__dict__.items():
    if isinstance(cls, ModelBase) and cls._meta.abstract is False:
        related_objects = cls._meta.get_all_related_objects()
        if related_objects:
            related_objects = [(related_object.related_name, classify(related_object.related_model._meta.verbose_name)) for related_object in related_objects]
            Meta = type(
                'Meta',
                (object,),
                {
                    'model': cls,
                    'fields': '__all__'
                }
            )
            # Dynamically create serializer name Ex: PollChoiceSerializer
            serializer_name = name
            for related_object in related_objects:
                serializer_name += related_object[1]
            serializer_name += 'Serializer'
            # Defining Serializer Class
            properties_dict = dict()
            for related_object in related_objects:
                properties_dict[related_object[0]] = globals()[related_object[1] + "Serializer"](many=True)
            properties_dict['Meta'] = Meta
            globals()[str(serializer_name)] = type(
                str(serializer_name),
                (serializers.ModelSerializer,),
                properties_dict
            )
