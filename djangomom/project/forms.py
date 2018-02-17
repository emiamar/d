from django import forms

from .models import Project
from account.models import UserAccount


class ProjectForm(forms.ModelForm):

    account = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Project
        fields = ('name', 'description', )
        # hidden_fields = ('account')

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['account'].widget = HiddenInput()

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        account = cleaned_data.get('account')
        user_account = UserAccount.objects.get(pk=account)
        project_count = user_account.projects.count()
        account_type = user_account.account_type
        if account_type is 2 and project_count >= 1:
            msg = "Sorry your account type is 'Base', Please switch to Pro account for more projects"
            self.add_error('name', msg)
