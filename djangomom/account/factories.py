import factory
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from .models import UserAccount, SignUp

User = get_user_model()


class SignUpFactory(DjangoModelFactory):

    email = 'admin@gdl.com'

    class Meta:
        model = SignUp


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username%d' % n)
    email = 'admin@gdl.com'
    password = 'admin@123'


class UserAccountFactory(DjangoModelFactory):
    class Meta:
        model = UserAccount
    user = factory.SubFactory(UserFactory)
    account_type = 1
