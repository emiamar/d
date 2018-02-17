from __future__ import absolute_import

from django.utils import timezone
from .utils import send_emails

from pyproduction.models import PyProduction

import logging
logger = logging.getLogger(__name__)


def item_production_mailer(*args, **kwargs):
    now = timezone.now().date()
    queryset = PyProduction.objects.filter(
        created_at__gte=now)
    context = dict()
    context['items'] = queryset
    context['title'] = "Items Produced on {0}!".format(
        now)
    if queryset:
        send_emails(
            to=['raoarun25@gmail.com'],
            bcc=['amar@greendesignlabs.in', 'arun@greendesignlabs.in'],
            subject='New Items created in pyfactory-cloud',
            template_name='pyproduction/daily_item_produced_mail.html',
            ctx=context,
        )
        return True
    else:
        logger.info('No items created today')
        return False
