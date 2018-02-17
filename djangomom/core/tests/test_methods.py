from django.test import TestCase

from pyproduction.factories import PaymentFactory

from core.methods import yesterday_collections


class CollectionTest(TestCase):
    def setUp(self):
        self.payment = PaymentFactory.create(
            amount=100, date='2016-05-30')
        self.payment = PaymentFactory.create(
            amount=500, date='2016-05-30')
        self.payment = PaymentFactory.create(
            amount=500, date='2016-05-31')

    def test_yesterday_collections(self):
        self.assertEqual(yesterday_collections(), 600)
