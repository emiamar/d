from django import forms

from .models import App
from .utils import validate_name


class AppForm(forms.ModelForm):

    class Meta:
        model = App
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget = HiddenInput()
        self.fields['need_migration'].widget = HiddenInput()
        self.fields['created_by'].widget = HiddenInput()

    def clean_name(self):
        data = self.cleaned_data['name']
        return data.lower()

    def clean(self):
        cleaned_data = super(AppForm, self).clean()
        name = cleaned_data.get("name")
        valid, message = validate_name(name)
        if not valid:
            self.add_error('name', message)
