# from djangomom.settings.base import BASE_DIR
import os
import re
import subprocess
import logging

from importlib import import_module

from djangomom.settings.base import BASE_DIR

from django.core.management import call_command

project_python_path = "/Users/amarsavalagi/Envs/djangomom/bin/python2.7"


project_directory = os.path.normpath(os.path.join(
    BASE_DIR, '../', '../', 'project_directory'))

logger = logging.getLogger(__name__)


def startapp(app_code_name):
    """
    Generates source codes, this method is
    equivalent to django startapp command.
    Needs app_code_name arg as foldername
    """
    folder = os.system('mkdir {0}/{1}'.format(
        project_directory,
        app_code_name
    )
    )
    if folder == 0:
        return call_command('startapp', app_code_name, '{0}/{1}'.format(
            project_directory,
            app_code_name),
            '--template=sampleapp'
        )
    else:
        return False


def startapp_v2(app_code_name, project_dir, *args, **kwargs):
    """
    Generates source app codes in new standalone poject,unlike the
    above method startapp which create app in own project under
    project_directory. This method is
    equivalent to django startapp command.
    Needs app_code_name arg as foldername
    """
    project_dir = os.path.abspath(project_dir)
    logger.debug(
        "About to creating app for project dir {0}".format(
            project_dir))
    app_path = "{0}/apps/{1}".format(project_dir, app_code_name)
    try:
        x = subprocess.Popen(
            ['mkdir', app_path]
        )
        print x
    except Exception as e:
        logger.error(e)
    try:
        x = subprocess.Popen(
            [
                project_python_path,
                '{0}/manage.py'.format(project_dir),
                'startapp',
                app_code_name, app_path,
                '--template=sampleapp'
            ]
        )
        print x
    except Exception as e:
        logger.error(e)


def app_management_command(
        app_code_name, project_dir, command, *args, **kwargs):
    # project_dir = os.path.abspath(project_dir)
    app_path = "{0}/apps/{1}".format(project_dir, app_code_name)
    x = subprocess.Popen(
        [
            project_python_path,
            '{0}/manage.py'.format(project_dir),
            command,
            app_code_name
        ]
    )
    print x
    return


def validate_name(app_name, app_or_project='app'):
    """
    Used to validate app and project name
    """
    # If it's not a valid directory name.
    if not re.search(r'^[_a-zA-Z]\w*$', app_name):
        # Provide a smart error message, depending on the error.
        if not re.search(r'^[_a-zA-Z]', app_name):
            message = 'make sure the app_name \
                begins with a letter or underscore'
        else:
            message = 'use only numbers, letters and underscores'
        error_message = "%r is not a valid %s name. Please %s.".format(
            app_name, app_or_project, message)
        return False, error_message
    try:
        import_module(app_name)
    except ImportError:
        return True, "Is Valid"
    else:
        return False, "Is invalid, {0} name can \
            not be existing python package name. Try another name.".format(
            app_or_project)

