from __future__ import unicode_literals
import logging

from django.db import models
from django.utils import timezone

from base.models import TimeStamp
from account.models import UserAccount
from mail.utils import send_emails

logger = logging.getLogger(__name__)


class Mail(TimeStamp):

    user_account = models.ForeignKey(UserAccount, null=True, blank=True)
    users = models.ManyToManyField(UserAccount, related_name='users')
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=300)
    body = models.TextField(
        max_length=5000, help_text="Use '|' for seperating paras")
    button = models.BooleanField(default=False)
    sent = models.DateTimeField(
        "Sent On", null=True, blank=True, editable=False)
    button_name = models.CharField(max_length=200, null=True, blank=True)
    button_path = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.user_account:
            return "{0}-{1}".format(
                self.user_account.user.username,
                self.subject
            )
        else:
            return self.subject

    def send_email(self):
        if not self.sent:
            if self.user_account or self.email:
                if self.user_account:
                    email = self.user_account.user.email
                    name = self.user_account.user.username
                else:
                    email = self.email
                    name = self.email.split("@")[0]
                self._prepare_mail(email, name)
            if self.users.exists():
                for user in self.users.all():
                    email = user.user.email
                    name = user.user.username
                    self._prepare_mail(email, name)
        else:
            logger.info('Email Already Sent')
            return "Already Sent"

    def _prepare_mail(self, email, name):
        context = {
            'name': name,
            'paras': self.body.split("|"),
            'button': self.button
        }
        if self.button:
            context['button_name'] = self.button_name
            context['button_path'] = self.button_path
        send_emails(
            subject=self.subject,
            to=[email],
            context=context,
            from_email='amar@apimonk.com',
            template_name='mail/generic_email.html'
        )
        self.sent = timezone.now()
        self.save()
