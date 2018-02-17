from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


from base.models import TimeStamp

import logging
logger = logging.getLogger(__name__)

INHERITOBJ = (
    (0, 'Contact'),
    (1, 'TimeStamp'),
)


class ModelObject(TimeStamp):

    app = models.ForeignKey('app.App')
    name = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name

    def fields_count(self):
        return self.modelfield_set.count()

    def code_name(self):
        # Return model name in django format EX: poll.Poll
        return '{1}.{0}'.format(self.name.capitalize(), self.app.name_lower)

    def app_code_name(self):
        # Return model name in django format
        # with app uuid prefixed EX: _safkljdkflsadfsf_poll.Poll
        return '{1}.{0}'.format(
            self.name.capitalize(), self.app.app_code_name)

    def unpack(self):
        import ast
        inheritance_list = [INHERITOBJ[int(obj)][1] for obj in ast.literal_eval(self.inherit)]
        return ','.join(inheritance_list)

    class Meta:
        unique_together = ("app", "name")

    def get_default_endpoints(self):
        endpoints = list()
        endpoints.append(
            dict(
                url='{2}/{0}/{1}_list/'.format(
                    self.app.name_lower,
                    self.name.lower(),
                    self.app.project.host_url
                ),
                model_name='{0} GET'.format(self.name.lower())
            )
        )
        endpoints.append(
            dict(
                url='{2}/{0}/{1}_detail/<object_id>'.format(
                    self.app.name_lower,
                    self.name.lower(),
                    self.app.project.host_url
                ),
                model_name='{0} GET'.format(self.name.lower())
            )
        )
        endpoints.append(
            dict(
                url='{2}/{0}/{1}_create/'.format(
                    self.app.name_lower,
                    self.name.lower(),
                    self.app.project.host_url
                ),
                model_name='{0} POST'.format(self.name.lower())
            )
        )
        endpoints.append(
            dict(
                url='{2}/{0}/{1}_update/<object_id>'.format(
                    self.app.name_lower,
                    self.name.lower(),
                    self.app.project.host_url
                ),
                model_name='{0} POST'.format(self.name.lower())
            )
        )
        endpoints.append(
            dict(
                url='{2}/admin/{0}/{1}/'.format(
                    self.app.name_lower,
                    self.name.lower(),
                    self.app.project.host_url
                ),
                model_name='{0} CRUD'.format(self.name.lower())
            )
        )
        return endpoints


FieldTypes = (
#    (1, 'AutoField'),
    (2, 'IntegerField'),
    (3, 'FloatField'),
    (4, 'DateField'),
    (5, 'DateTimeField'),
    (6, 'EmailField'),
    (7, 'TimeField'),
    (8, 'DecimalField'),
    (9, 'CharField'),
    (10, 'SlugField'),
    (11, 'TextField'),
    (12, 'URLField'),
    (13, 'BigIntegerField'),
    (14, 'SmallIntegerField'),
    (15, 'PositiveSmallIntegerField'),
    (16, 'BooleanField'),
    (17, 'ForeignKey'),
    (18, 'ManyToManyField'),
    (19, 'OneToOneField'),
    (20, 'DurationField')
)


class ModelField(TimeStamp):

    model_obj = models.ForeignKey(ModelObject)
    name = models.SlugField(max_length=50)
    field_type = models.IntegerField(
        blank=True, choices=FieldTypes)
    max_length = models.IntegerField(blank=True, null=True)
    default = models.CharField(max_length=50, blank=True, null=True)
    blank = models.BooleanField(default=False)
    null = models.BooleanField(default=True)
    foreign_key = models.CharField(max_length=100, blank=True, null=True)
    many_to_many_key = models.CharField(max_length=50, blank=True, null=True)
    related_name = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return "{0}-{1}".format(self.model_obj, self.name)

    class Meta:
        unique_together = ('model_obj', 'name')


@receiver(post_save, sender=ModelField, dispatch_uid="prepare_app")
def prepare_app(sender, instance, **kwargs):
    instance.model_obj.app.prepare_app()
    import time
    time.sleep(0.5)
    instance.model_obj.app.migrate()
    if instance.model_obj.modelfield_set.count() == 1:
        add_permissions(instance)


def add_permissions(instance):
    import requests
    from django.conf import settings
    url = '{0}/perm/add/'.format(instance.model_obj.app.project.host_url)
    data = {
        'username': instance.model_obj.app.created_by.username,
        'app_label': instance.model_obj.app.name_lower,
        'model': instance.model_obj.name.lower(),
        'SECRET_KEY': settings.SECRET_KEY
    }
    try:
        response = requests.get(url, data)
        if response.status_code != 200:
            logger.critical(
                'Some serious error \
                    while adding perms: Response{0}'.format(
                    response.content))
        else:
            logger.info("Response: {0}".format(response.content))
    except requests.ConnectionError:
        logger.error("ERROR in connecting to secondary server")


QUERYSETTYPE = (
    ('LIST', 'List'),
    ('SINGLE', 'Single'),
)


class QuerySet(TimeStamp):

    name = models.CharField(max_length=100)
    model = models.ForeignKey('modeller.ModelObject', null=True)
    queryset_type = models.CharField(max_length=10, choices=QUERYSETTYPE)
    order_paramater = models.ForeignKey(
        'modeller.ModelField', null=True, blank=True)
    reverse = models.BooleanField(default=False)
    get_all = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def query_method(self):
        if self.get_all:
            return 'objects.all()'
        elif self.queryset_type == 'LIST':
            filter_string = 'objects.'
            for query_filter in self.querysetfilter_set.all():
                filter_string += query_filter.get_filter_string()
            return filter_string
        else:
            return 'objects.get()'


FILTEROPERATION = (
    ('gte', 'Greater Than'),
    ('lte', 'Less Than'),
    ('contains', 'Contains'),
    ('exact', 'exact'),
    ('isnull', 'Is Null'),
    ('startswith', 'Starts With'),
    ('endswith', 'Ends With'),
)

FILTERTYPE = (
    ('exclude', "Exclude"),
    ('filter', "Include")
)


class QuerySetFilter(TimeStamp):

    filter_type = models.CharField(max_length=10, choices=FILTERTYPE)
    queryset = models.ForeignKey('modeller.QuerySet')
    paramater = models.ForeignKey('modeller.ModelField')
    operation = models.CharField(
        max_length=10, choices=FILTEROPERATION, null=True, blank=True)
    filter_value = models.CharField(max_length=5000)

    def get_filter_string(self):
        if self.operation:
            return '{0}({1}__{2}="{3}")'.format(
                self.filter_type,
                self.paramater.name,
                self.operation,
                self.filter_value
            )
        else:
            return '{0}({1}="{2}")'.format(
                self.filter_type,
                self.paramater.name,
                self.filter_value
            )



