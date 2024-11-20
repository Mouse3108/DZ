from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('avatar', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('avatar', 'username', 'email', 'first_name', 'last_name')
    fieldsets = UserAdmin.fieldsets + (('Аватар', {'fields': ('avatar',)}),)
