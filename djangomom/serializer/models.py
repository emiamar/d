from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp
from modeller.models import FieldTypes


class SerializerObject(TimeStamp):

    name = models.CharField(max_length=100)
    model = models.ForeignKey('modeller.ModelObject')
    field_parms = models.ManyToManyField('modeller.ModelField')


class CustomField(TimeStamp):

    serializer_object = models.ForeignKey('serializer.SerializerObject')
    field_type = models.IntegerField(
        blank=True, choices=FieldTypes)
