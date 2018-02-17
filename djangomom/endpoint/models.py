from __future__ import unicode_literals

from django.db import models

from base.models import TimeStamp


class EndPoint(TimeStamp):

    name = models.CharField(max_length=100, null=True)
    app = models.ForeignKey(
        'app.App', related_name='endpoints', null=True)
    url = models.CharField(max_length=200)
    serializer_object = models.ForeignKey(
        'serializer.SerializerObject', null=True)
    queryset = models.ForeignKey('modeller.QuerySet', null=True)

    def __unicode__(self):
        return "({0}){1}".format(self.url, self.app)

    # def write_end_point(self):


QUANTA_TYPE = (
    ('DIC', 'Dictionary'),
    ('ARY', 'Array'),
    ('INT', 'Intiger'),
    ('STR', 'String'),
    ('DT', 'DateTime'),
)


class Quanta(TimeStamp):

    key = models.CharField(max_length=100)
    quanta_type = models.CharField(max_length=3, choices=QUANTA_TYPE)
    value = models.CharField(max_length=100, null=True, blank=True)
    root = models.ForeignKey('Quanta', null=True, blank=True)
