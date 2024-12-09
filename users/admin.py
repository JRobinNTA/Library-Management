from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'membership_type', 'is_staff', 'registered_date']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('membership_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('membership_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)