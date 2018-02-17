from django.test import TestCase

from account.factories import SignUpFactory

from project.factories import ProjectFactory

from account.models import UserAccount

from mock import patch


class UserRegisterationTest(TestCase):

    def setUp(self):
        self.signup = SignUpFactory(
            email='test_user_registeration@apimonk.com')
        self.project = ProjectFactory(name="djangomom_template_project")

    @patch('account.models.add_user')
    @patch('mail.utils.send_emails')
    def test_user_registeration(self, add_user_mock, send_emails_mock):
        self.signup.create_user_account()
        user_count = UserAccount.objects.count()
        self.assertEqual(user_count, 1)
        user = UserAccount.objects.get(
            user__username="test_user_registeration")
        self.assertEqual(user.account_type, 2)
        self.assertTrue(self.signup.is_ready)
        accounts = self.project.account.all()
        self.assertTrue(user in accounts)
