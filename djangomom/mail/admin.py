from django.contrib import admin
from .models import Mail


def send_mail(modeladmin, request, queryset):
    for user in queryset:
        user.send_email()


class MailAdmin(admin.ModelAdmin):

    list_display = (
        'user_account', 'subject', 'sent',
        'created_at', 'updated_at')
    list_filter = ('created_at', )
    search_fields = (
        'user_account__user__username',
        'subject',
        'email'
    )
    actions = [send_mail]


admin.site.register(Mail, MailAdmin)
