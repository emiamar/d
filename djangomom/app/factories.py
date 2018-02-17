import factory

# from django.contrib.auth.models import User

from factory.django import DjangoModelFactory

from .models import App

from project.factories import ProjectFactory


class AppFactory(DjangoModelFactory):
    class Meta:
        model = App
    project = factory.SubFactory(ProjectFactory)
    name = 'test_app'
