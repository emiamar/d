from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib import messages
from django.shortcuts import HttpResponseRedirect

from base.views import GenericDataGridView, GenericModalCreateView
from base.mixin import GeneralContextMixin

from models import Project
from forms import ProjectForm


class ProjectListView(GeneralContextMixin, GenericDataGridView):

    model = Project
    template_name = "project/index.html"
    context_object_name = 'projects'
    list_display = (
        ('Name', 'name'),
        ('Apps Count', 'apps_count'),
        ('Created on', 'created_at'),
        ('Last updated', 'updated_at'),
    )
    title = 'List of Projects'
    sub_title = ''
    # date_range = True
    detail_url_reverse = 'apps:index'

    def make_query(self, **kwargs):
        return self.model.objects.filter(account__user=self.request.user)


class CreateProjectView(GenericModalCreateView):

    model = Project
    form_class = ProjectForm
    success_url = '/dashboard/'
    permission_required = 'project.add_project'

    def form_init(self, request, *args, **kwargs):
        data = request.POST.copy()
        account_id = request.user.useraccount.pk
        data['account'] = account_id
        form = self.form_class(data)
        return self.form_check(form, *args, **kwargs)

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        msg = "Sorry your account type is 'Base'. "
        msg = msg + "Please switch to 'Pro' account to create more projects"
        mgs = msg +  "Or Try creating app in existing djangomom_template_project below"
        messages.warning(self.request, msg)
        return HttpResponseRedirect(self.get_error_url())

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        print "Form valid"
        form.save()
        instance = form.instance
        instance.account.add(self.request.user.useraccount)
        instance.save()
        msg = "Succesfully created new {0} {1}".format(
            self.object_name, form.instance)
        print "Form Saved"
        messages.success(self.request, msg)
        return HttpResponseRedirect(self.get_success_url())
