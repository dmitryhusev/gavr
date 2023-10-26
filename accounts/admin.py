from .models import Users

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ("email", "id", "first_name", "last_name", "is_superuser", "is_active")
    list_filter = ()
    ordering = ("-id",)
    fieldsets = ()
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('email', 'password1', 'password2'),
                },
            ),
        )

admin.site.register(Users, CustomUserAdmin)
