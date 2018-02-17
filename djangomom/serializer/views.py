from base.mixin import GeneralContextMixin
from base.v2.generic_data_grid_view import GenericDataTableView

from models import SerializerObject


class AppSerializerObjectListView(GeneralContextMixin, GenericDataTableView):

    model = SerializerObject
    template_name = "serializer/index.html"
    list_display = [
        'name',
        'created_at',
        'updated_at',
    ]
    title = 'Data Serializer'
    sub_title = 'Manage you data representation'
    # detail_page = 'models:detail'

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(model__app=self.kwargs.get('pk'))

    # def get_context_data(self, **kwargs):
    #     context = super(
    #         AppSerializerObjectListView, self).get_context_data(**kwargs)
    #     context['form'] = ModelObjectForm()
    #     context['app'] = self.kwargs.get('pk')
    #     return context