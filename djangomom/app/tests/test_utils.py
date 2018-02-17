import os
import uuid

from django.test import TestCase

from app.utils import startapp, project_directory


class StartAppTest(TestCase):

    def setUp(self):
        self.app_code_name = '_{0}_startapp_test_app'.format(uuid.uuid4().hex)
        startapp(self.app_code_name)

    def test_start_app(self):
        is_file = os.path.isfile(
            '{0}/{1}/models.py'.format(
                project_directory, self.app_code_name))
        self.assertTrue(is_file)
        is_deleted = os.system(
            "rm -r {0}/{1}".format(
                project_directory,
                self.app_code_name)
        )
        self.assertEquals(is_deleted, 0)
