from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', )

admin.site.register(Project, ProjectAdmin)
