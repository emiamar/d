from django.contrib import messages

from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView

from base.mixin import GeneralContextMixin
from base.v2.generic_data_grid_view import GenericDataTableView
from base.views import GenericSelfRedirection


from models import App
from forms import AppForm


class ProjectAppListView(GeneralContextMixin, GenericDataTableView):
    """
    Renders the page for listing and managing pages for given project
    """
    model = App
    template_name = "app/index.html"
    list_display = [
        'name',
        'total_models',
        'source_code_available',
        'created_at',
        'updated_at',
    ]
    title = 'List of Apps'
    sub_title = 'Manage you apps'
    date_range = False
    detail_page = 'models:index'
    action_dict = {
        # Turned to automation
        # "Generate Source code": 'generate_source_code',
        # "Write models": 'write_models',
        # "Make Migrations": 'makemigrations',
        # "Migrate": 'migrate'
    }

    def get_queryset(self):
        return App.objects.filter(
            created_by=self.request.user).filter(project=self.kwargs.get('pk'))

    #################################################
    # #########Out Dated because automation############
    # def generate_source_code(self):
    #     apps = App.objects.filter(pk__in=self.for_action_keys)
    #     for app in apps:
    #         if not app.generate_codes():
    #             messages.error(
    #                 self.request,
    #                 "Source code for app {0} already generated".format(
    #                     app.name)
    #             )
    #     return self.success_url()

    # def write_models(self):
    #     apps = App.objects.filter(pk__in=self.for_action_keys)
    #     for app in apps:
    #         app.write_models()
    #     return self.success_url()

    # def makemigrations(self):
    #     apps = App.objects.filter(pk__in=self.for_action_keys)
    #     for app in apps:
    #         app.makemigrations()
    #     return self.success_url()

    # def migrate(self):
    #     apps = App.objects.filter(pk__in=self.for_action_keys)
    #     for app in apps:
    #         app.migrate()
    #     return self.success_url()

    def success_url(self):
        return HttpResponseRedirect('/apps/{0}/'.format(self.kwargs.get('pk')))

    def get_context_data(self, **kwargs):
        context = super(
            ProjectAppListView, self).get_context_data(**kwargs)
        context['form'] = AppForm()
        context['project_id'] = self.kwargs.get('pk')
        return context


class ResourcesListView(GeneralContextMixin, GenericDataTableView):
    template_name = 'app/resources_list.html'
    model = App

    list_display = [
        'model_name',
        'url'
    ]
    title = 'List of Resources'
    sub_title = 'API endpoints'

    def get_queryset(self):
        return App.objects.get(
            pk=self.kwargs.get('pk')).get_default_endpoints()


class AppCreateView(GenericSelfRedirection):

    form_class = AppForm
    object_name = 'App'
    url_pattern_list = ['models']

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        self.project = request.POST.get('_project')
        data['project'] = self.project
        data['created_by'] = request.user.id
        form = self.form_class(data)
        return self.form_check(form, *args, **kwargs)

    def get_error_url(self):
        return '/apps/{0}'.format(self.project)

    def get_error_message(self, form):
        msg = "Sorry unable to create new app. {0}".format(form.errors.as_text())
        print type(msg)
        return msg

    def get_success_message(self, form):
        msg = "Great New app {0} is ready lets add new DataStore an table to store data".format(
            form.instance.name)
        return msg
