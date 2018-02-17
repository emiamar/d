from django.conf.urls import url

import views

urlpatterns = [
    # List of serializer for a perticular app
    url(r'^list/(?P<pk>[^/]+)/$',
        views.AppSerializerObjectListView.as_view(),
        name='serializer_list'),
]
