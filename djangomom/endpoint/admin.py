from django.contrib import admin

from .models import EndPoint


class EndPointAdmin(admin.ModelAdmin):

    list_display = ('url', 'created_at', 'updated_at')
    list_filter = ('created_at', )


admin.site.register(EndPoint, EndPointAdmin)
