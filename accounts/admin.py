from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import HaruuUser
from api.models import EmailConfirm


class HaruuAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'application')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class EmailConfirmAdmin(admin.ModelAdmin):
    list_display = ('id', 'after_change_email', 'token', 'haruu_user')
    fieldsets = [
        (None, {'fields': ('after_change_email', 'token')}),
    ]


admin.site.register(HaruuUser, HaruuAdmin)
admin.site.register(EmailConfirm, EmailConfirmAdmin)
