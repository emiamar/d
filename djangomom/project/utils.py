from django.conf import settings

import os
import subprocess


def create_project(project_name):
    # To DO
    # Need to write service to create project in webfaction cloud machines
    os.environ['DJANGO_SETTINGS_MODULE'] = ''
    try:
        project_dir = '{1}{0}/{0}'.format(
            project_name, settings.PROJECTS_DIRECTORY)
        x = subprocess.Popen(
            ['mkdir', '{1}{0}'.format(
                project_name, settings.PROJECTS_DIRECTORY)],
            stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
        )
        x = subprocess.Popen(
            ['mkdir', project_dir]
        )
        print x
        import time
        time.sleep(3)
    except:
        raise
    try:
        x = subprocess.Popen(
            ['django-admin.py', 'startproject',
            '{0}'.format(project_name), project_dir,
            '--template=https://bitbucket.org/asavalagi/project_name/get/template.zip'
            ]
        )
        print x
    except:
        raise
    os.environ['DJANGO_SETTINGS_MODULE'] = 'djangomom.local'