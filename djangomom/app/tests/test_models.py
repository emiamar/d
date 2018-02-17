import os
from django.test import TestCase

from app.factories import AppFactory
from app.utils import project_directory


class AppModelTest(TestCase):

    def setUp(self):
        self.app = AppFactory()

    def test_source_code_available(self):
        self.assertFalse(
            self.app.source_code_available()
        )

    def test_generate_codes(self):
        self.app.generate_codes()
        self.assertTrue(
            self.app.source_code_available()
        )
        os.system(
            "rm -r {0}/{1}".format(
                project_directory,
                self.app.app_code_name)
        )
