from __future__ import unicode_literals
import os

from django.db import models
from django.conf import settings

from base.models import TimeStamp

# from account.models import UserAccount

from project.utils import create_project


import logging
logger = logging.getLogger(__name__)


DataBases = (
    (1, 'sqlite3'),
    (2, 'postgresql_psycopg2'),
)


class Project(TimeStamp):
    # ToDo: Need to make name unique field
    name = models.SlugField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    data_base = models.IntegerField(
        null=True, blank=True, choices=DataBases)
    is_created = models.BooleanField(default=False)
    account = models.ManyToManyField(
        'account.UserAccount', related_name='projects')
    host_url = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    @property
    def clean_project_name(self):
        # ToDo:
        # Need to do sanity check on project name and add loging
        return self.name.lower()

    def project_dir(self):
        """
        Method returning absolute path to project as str
        """
        return os.path.join(
            settings.PROJECTS_DIRECTORY,
            self.clean_project_name,
            self.clean_project_name)

    def apps_count(self):
        return self.app_set.count()

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            try:
                create_project(project_name=self.clean_project_name)
            except Exception as e:
                logger.exception('Unable to run create_project {0}'.format(e))
        return super(self.__class__, self).save(*args, **kwargs)
