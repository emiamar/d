from django.contrib import admin

from serializer.models import SerializerObject, CustomField


class CustomFieldInline(admin.TabularInline):
    model = CustomField
    extra = 3


class SerializerObjectAdmin(admin.ModelAdmin):

    inlines = [CustomFieldInline]
    list_display = ('name', 'model', 'created_at', 'updated_at')
    # list_filter = ('app', 'created_at')


admin.site.register(
    SerializerObject, SerializerObjectAdmin)
