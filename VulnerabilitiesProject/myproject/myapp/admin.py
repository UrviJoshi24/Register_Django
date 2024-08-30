# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # List the fields to be displayed in the admin
    list_display = ('username', 'email_id', 'name', 'contact_number', 'gender', 'is_staff', 'is_active')
    # Define the fields used in forms for creating and updating users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'contact_number', 'email_id', 'gender')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'contact_number', 'email_id', 'gender')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
