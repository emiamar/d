import os
import subprocess

from django.test import TestCase

from ..factories import ProjectFactory


class ProjectCreateUtilsTest(TestCase):

    def setUp(self):
        self.project = ProjectFactory()

    def test_project_dir_method(self):
        is_path = os.path.isdir(self.project.project_dir())
        self.assertTrue(is_path)
        print os.path.realpath(self.project.project_dir())
        os.system('rm -r {0}'.format(os.path.realpath(self.project.project_dir())))