import django.dispatch

models_ready = django.dispatch.Signal(providing_args=["project_name"])
