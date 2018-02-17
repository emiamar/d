from django import forms

from .models import ModelObject, ModelField, INHERITOBJ

import logging
logger = logging.getLogger(__name__)


class ModelObjectForm(forms.ModelForm):
    inherit = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=INHERITOBJ, required=False
    )

    class Meta:
        model = ModelObject
        fields = '__all__'


class ModelFieldForm(forms.ModelForm):
    # foreign_key = forms.ChoiceField(choices=options, required=False)
    foreign_key = forms.ChoiceField(required=False)
    many_to_many_key = forms.ChoiceField(required=False)

    class Meta:
        model = ModelField
        exclude = ('null',)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        user = kwargs.pop('user')
        super(ModelFieldForm, self).__init__(*args, **kwargs)
        self.fields['model_obj'].widget = HiddenInput()
        self.fields['model_obj'].value = "New Field name"
        if not user:
            logger.critical("User not provided")
        options = [(model_obj.code_name(), model_obj.code_name()) for model_obj in ModelObject.objects.filter(app__created_by=user)]
        options.insert(0, ('', 'Select'))
        self.fields['foreign_key'].choices = options
        self.fields['many_to_many_key'].choices = options

    def clean(self):
        cleaned_data = super(ModelFieldForm, self).clean()
        field_type = cleaned_data.get("field_type")
        max_length = cleaned_data.get("max_length")

        if field_type in (11, 9, 10) and max_length is None:
            msg = "Char, Slug and TextField need max_length defined"
            self.add_error('max_length', msg)
