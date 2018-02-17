from __future__ import unicode_literals
import os

from django.db import models
from django.template.loader import get_template

from django.dispatch import receiver

from base.models import TimeStamp
from modeller.models import ModelObject
from endpoint.models import EndPoint

from .utils import startapp_v2, app_management_command
from .signals import models_ready

import logging
logger = logging.getLogger(__name__)


class App(TimeStamp):

    project = models.ForeignKey('project.Project')
    name = models.SlugField(max_length=50, unique=True)
    need_migration = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', null=True, blank=True)

    class Meta:
        unique_together = ("name", "project")

    def __unicode__(self):
        return "{0}-{1}".format(self.project, self.name)

    def total_models(self):
        return self.modelobject_set.count()

    @property
    def name_lower(self):
        """
        """
        return self.name.lower()

    @property
    def app_code_name(self):
        """
        Returns appname as string appended with UUID,
        which is used as app folder name"""
        return "_{1}_{0}".format(self.name, self.project_id.hex)

    def source_code_available(self):
        """
        """
        return os.path.isdir(
            "{0}/apps/{1}/".format(
                self.project.project_dir(), self.name_lower))

    def generate_codes(self):
        """
        Generates source codes, this method is
        equivalent to django startapp command.
        """
        if not self.source_code_available():
            startapp_v2(
                self.name_lower,
                project_dir=self.project.project_dir())
            return True
        else:
            return False

    def write_models(self):
        # Need to Depricate below codes
        self.need_migration = True
        self.save()
        ####
        template = get_template('modeller/base_models.py')
        context = {
            'model_objects': ModelObject.objects.filter(app=self)
        }
        result = template.render(context)
        f = open(
            '{1}/apps/{0}/models.py'.format(
                self.name_lower,
                self.project.project_dir()),
            'w')
        f.write(result)
        f.close()
        # Writes an empty file in methods folder
        model_list = list()
        for model in self.modelobject_set.all():
            model_list.append(model.name.lower())
            model_file = open(
                '{1}/apps/{0}/methods/{2}.py'.format(
                    self.name_lower,
                    self.project.project_dir(),
                    model.name.lower()),
                'w')
            model_file.write('')
            model_file.close()
        # Writes import in __init__ file of methods folder
        init_file = open(
            '{1}/apps/{0}/methods/__init__.py'.format(
                self.name_lower,
                self.project.project_dir()),
            'w')
        imports = ','.join(model_list)
        init_file.write('import {0}'.format(imports))
        init_file.close()
        models_ready.send(
            sender=None, project_name=self.project.clean_project_name)
        return True

    def makemigrations(self):
        # call_command('makemigrations', self.app_code_name, interactive=False)
        app_management_command(
            self.name_lower,
            self.project.project_dir(),
            'makemigrations'
        )

    def migrate(self):
        # call_command('migrate', self.app_code_name, interactive=False)
        app_management_command(
            self.name_lower,
            self.project.project_dir(),
            'migrate'
        )

    def get_default_endpoints(self):
        endpoints = list()
        # endpoints.append(args)
        for model in self.modelobject_set.all():
            endpoints += model.get_default_endpoints()
        return endpoints

    def write_views(self):
        template = get_template('endpoint/base_views.py')
        context = {
            'endpoints': EndPoint.objects.filter(app=self)
        }
        result = template.render(context)
        f = open(
            '{1}/apps/{0}/autogen_views.py'.format(
                self.name_lower,
                self.project.project_dir()),
            'w')
        f.write(result)
        f.close()

    def prepare_app(self):
        print "Writting models"
        self.write_models()
        print "Running Makemigrations"
        self.makemigrations()

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            self.generate_codes()
        return super(self.__class__, self).save(*args, **kwargs)


@receiver(models_ready)
def restart_server(project_name, **kwargs):
    print "Restarting the server"
    print project_name
    try:
        os.system(
            "~/./webapps/{0}/apache2/bin/restart".format(
                project_name))
        print "Server Restarted.."
    except Exception as e:
        logger.exception(e)
        print "Couldnt not restart the server"

