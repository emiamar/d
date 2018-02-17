from __future__ import unicode_literals
import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from mail.utils import send_emails

from base.models import TimeStamp

from project.models import Project


import logging
logger = logging.getLogger(__name__)

DOC_ATTACHMENT = os.path.normpath(
    os.path.join(settings.BASE_DIR, '../', '../' 'APImonk.pdf')
)

ACCOUNT_TYPE = (
    (1, 'PRO'),
    (2, 'BASE'),
)

DEFAULT_PASSWORD = 'admin@123'

DEFAULT_PROJECT = 'djangomom_template_project'

DEMO_PROJECT_LINK = 'http://demo.apimonk.com'


class UserAccount(TimeStamp):
    user = models.OneToOneField(User)
    account_type = models.IntegerField(
        blank=True, choices=ACCOUNT_TYPE)

    def __unicode__(self):
        return "{0}".format(self.user.username)

    def send_registeration_email(self):
        send_emails(
            to=[self.user.email],
            subject='Welcome to APImonk',
            from_email='amar@apimonk.com',
            template_name='mail/introduction_email.html',
            context={
                'name': self.user.username,
                'username': self.user.username,
                'password': DEFAULT_PASSWORD
            },
            attachment=DOC_ATTACHMENT
        )


def add_user(username, password=DEFAULT_PASSWORD):
    """
    Creates user on demo server
    """
    import requests
    from django.conf import settings
    url = '{0}/perm/add_user/'.format(DEMO_PROJECT_LINK)
    data = {
        'username': username,
        'password': password,
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


class SignUp(TimeStamp):
    email = models.EmailField(max_length=100)
    is_ready = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email

    def create_user_account(self, password=DEFAULT_PASSWORD, account_type=2):
        username = self.email.split("@")[0]
        try:
            user = User.objects.create(
                username=username,
                email=self.email)
            user.set_password(password)
            user.save()
        except Exception as e:
            logger.error(e)
            return
        account = UserAccount.objects.create(
            user=user,
            account_type=account_type)
        account.save()
        try:
            project = Project.objects.get(name=DEFAULT_PROJECT)
            project.account.add(account)
            project.save()
        except Exception as e:
            logger.error(e.message)
        add_user(username)
        account.send_registeration_email()
        self.is_ready = True
        self.save()
        return account

    class Meta:
        ordering = ['-created_at']

