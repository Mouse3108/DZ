from django.contrib import admin
from .models import *


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'phone', 'comment')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_info')
    search_fields = ('first_name', 'last_name', 'contact_info')
    list_filter = ('services',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'price')
    
