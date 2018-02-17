from django import forms

from .models import SignUp

from base.views import GenericModalCreateView


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ('email', )


class SignUpView(GenericModalCreateView):

    form_class = SignUpForm
    success_url = '/'
    object_name = 'SignUp'
