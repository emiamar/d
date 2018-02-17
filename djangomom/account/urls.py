from django.conf.urls import url

import views

urlpatterns = [
    # Creates new SignUp
    url(r'^signup/$',
        views.SignUpView.as_view(),
        name='signup'),
]
