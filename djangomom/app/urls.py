from django.conf.urls import url

import views

urlpatterns = [
    # Creates new App Obj
    url(r'^create/$',
        views.AppCreateView.as_view(),
        name='create'),
    url(r'^resources_list/(?P<pk>[^/]+)/$',
        views.ResourcesListView.as_view(),
        name='resources_list'),
    # Project deatil or list of app for specific project.
    url(r'^(?P<pk>[^/]+)/$',
        views.ProjectAppListView.as_view(),
        name='index'),
]
