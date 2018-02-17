from django.utils import timezone

from pyproduction.models import Payment


def yesterday_collections():
    total = 0
    payments = Payment.objects.filter(
        date=(timezone.now() + timezone.timedelta(days=-1)).date())
    for payment in payments:
        amount = payment.amount
        total = total + amount
    return total


def due_cheques():
    payments = Payment.objects.all()
    payments = [
        payment for payment in payments if payment.payment_mode is 2 and payment.is_cheque_due()
    ]
    return payments
