from django.contrib import admin

from .models import UserAccount, SignUp


def register_user(modeladmin, request, queryset):
    for user in queryset:
        user.create_user_account()


class UserAccountAdmin(admin.ModelAdmin):

    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('created_at', )


class SignUpAdmin(admin.ModelAdmin):

    list_display = ('email', 'is_ready', 'created_at', 'updated_at')
    list_filter = ('created_at', )
    actions = [register_user]


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
