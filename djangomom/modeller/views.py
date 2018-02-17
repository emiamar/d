from base.views import (
    GenericSelfRedirection, GenericModalCreateView)
from base.mixin import GeneralContextMixin
from base.v2.generic_data_grid_view import GenericDataTableView

from models import ModelObject, ModelField
from forms import ModelObjectForm, ModelFieldForm


class AppModelObjectListView(GeneralContextMixin, GenericDataTableView):

    model = ModelObject
    template_name = "modeller/index.html"
    list_display = [
        'name',
        'created_at',
        'updated_at',
    ]
    title = 'Data Store'
    sub_title = 'Manage you data models'
    detail_page = 'models:detail'

    def get_queryset(self, **kwargs):
        return ModelObject.objects.filter(app=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(
            AppModelObjectListView, self).get_context_data(**kwargs)
        context['form'] = ModelObjectForm()
        context['app'] = self.kwargs.get('pk')
        return context


class ModelObjectDetailView(GeneralContextMixin, GenericDataTableView):

    model = ModelField
    template_name = "modeller/detail.html"
    list_display = [
        'name',
        'get_field_type_display',
        'null',
        'blank',
        'created_at',
        'updated_at',
    ]
    title = 'List Fields'
    sub_title = 'Build your data store'
    date_range = False

    def get_queryset(self, **kwargs):
        return ModelField.objects.filter(model_obj=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(
            ModelObjectDetailView, self).get_context_data(**kwargs)
        context['form'] = ModelFieldForm(user=self.request.user)
        context['model_obj_id'] = self.kwargs.get('pk')
        return context


class ModelObjectCreateView(GenericSelfRedirection):

    form_class = ModelObjectForm
    object_name = 'Transaction'
    url_pattern_list = ['models', 'detail']

    def get_error_url(self):
        return '/models/{0}'.format(self.request.POST['app'])

    def get_error_message(self, form):
        return "Sorry unable to create new DataStore. DataStore {0}".format(
            form.errors.as_text())

    def get_success_message(self, form):
        return "Great new DataStore {0} is created. Lets add fields or columns for you DataStore".format(form.instance.name)


class ModelFieldCreateView(GenericModalCreateView):

    form_class = ModelFieldForm
    object_name = 'Field'

    def get_success_url(self):
        return '/models/detail/{0}'.format(self.request.POST['model_obj_id'])

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        data['model_obj'] = self.request.POST.get('model_obj_id')
        form = self.form_class(data, user=request.user)
        return self.form_check(form, *args, **kwargs)

    # def form_valid(self, form):
    #     instance = form.instance
    #     instance.model_obj = ModelObject.objects.get(
    #         pk=self.request.POST.get('model_obj'))
    #     return super(ModelFieldCreateView, self).form_valid(form)

    def get_error_message(self, form):
        return "Sorry unable to create new Field. {0} ".format(
            form.errors.as_text())

    def get_success_message(self, form):
        return "Great new Field {0} is created.".format(
            form.instance.name,
        )
