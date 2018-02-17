import factory
from factory.django import DjangoModelFactory

from .models import Project

from account.factories import UserAccountFactory


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project
    name = 'test_project'
    # account = factory.SubFactory(UserAccountFactory)
    data_base = 1
