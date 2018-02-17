from django.views.generic import TemplateView

from base.mixin import GeneralContextMixin


class AddResourceView(GeneralContextMixin, TemplateView):

    template_name = 'endpoint/add_resource.html'
