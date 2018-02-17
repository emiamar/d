import logging

from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

logger = logging.getLogger(__name__)


def send_emails(
    to=None, subject='', from_email='',
    context={}, template_name='', bcc=None, attachment=None
):
    message = get_template(
        template_name).render(Context(context))
    msg = EmailMessage(subject, message, to=to, from_email=from_email, bcc=bcc)
    msg.content_subtype = 'html'
    if attachment:
        msg.attach_file(attachment)
    try:
        msg.send()
    except Exception as e:
        logger.error(e.message)
        logger.debug("Sending failed..! Plz verify email id")
    print "Email sent"
