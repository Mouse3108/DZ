from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('display_photo', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_display_links = ('display_photo', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    list_editable = ('is_staff', 'is_superuser')
    readonly_fields = ('show_photo',)

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" />', obj.avatar.url)
    display_photo.short_description = 'Мини-аватар'

    def show_photo(self, obj):
        return format_html('<img src="{}" width="200" />', obj.avatar.url)
    show_photo.short_description = 'Аватар'

    fieldsets = UserAdmin.fieldsets + (('Аватар', {'fields': ('show_photo', 'avatar',)}),)
