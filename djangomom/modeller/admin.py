from django.contrib import admin

from modeller.models import ModelObject, ModelField, QuerySetFilter, QuerySet


class ModelFieldInline(admin.TabularInline):
    model = ModelField
    extra = 3


class ModelObjectAdmin(admin.ModelAdmin):

    inlines = [ModelFieldInline]
    list_display = ('name', 'app', 'created_at', 'updated_at')
    list_filter = ('app', 'created_at')


class QuerySetFilterInline(admin.TabularInline):
    model = QuerySetFilter
    extra = 3


class QuerySetAdmin(admin.ModelAdmin):

    inlines = [QuerySetFilterInline]
    list_display = ('name', 'model', 'created_at', 'updated_at')
    list_filter = ('created_at',)


admin.site.register(QuerySet, QuerySetAdmin)
admin.site.register(ModelObject, ModelObjectAdmin)
