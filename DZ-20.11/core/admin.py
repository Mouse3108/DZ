from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'status', 'master')
    list_display_links = ('name', 'phone', 'date', 'master')
    list_filter = ('status', 'date', 'master')
    search_fields = ('name', 'phone', 'comment')
    list_editable = ('status',)
    filter_horizontal = ('services',)
    readonly_fields = ('date',)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('display_photo', 'first_name', 'last_name', 'contact_info')
    list_display_links = ('display_photo', 'first_name', 'last_name', 'contact_info')
    search_fields = ('first_name', 'last_name', 'contact_info')
    list_filter = ('services',)

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" />', obj.photo.url)
    display_photo.short_description = 'Фото'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'price')
    
