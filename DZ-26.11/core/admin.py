from django.contrib import admin
from django import forms
from .models import *
from django.utils.html import format_html
import datetime


class TimeFilter(admin.SimpleListFilter):
    title = 'Время суток'
    parameter_name = 'time_of_day'

    def lookups(self, request, model_admin):
        return (
            ('morning', 'Утро (6:00-12:00)'),
            ('afternoon', 'День (12:01-18:00)'),
            ('evening', 'Вечер (18:01-23:59)'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'morning':
            return queryset.filter(date__time__gte=datetime.time(6, 0), date__time__lt=datetime.time(12, 0))
        if self.value() == 'afternoon':
            return queryset.filter(date__time__gte=datetime.time(12, 1), date__time__lt=datetime.time(18, 0))
        if self.value() == 'evening':
            return queryset.filter(date__time__gte=datetime.time(18, 1))
        return queryset


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'status', 'master', 'visit_number')
    actions = ['set_unconfirmed', 'set_confirmed', 'set_cancelled', 'set_completed']
    list_display_links = ('name', 'phone', 'date')
    list_filter = ('status', 'date', 'master', TimeFilter)
    search_fields = ('name', 'phone', 'comment')
    list_editable = ('status', 'master')
    filter_horizontal = ('services',)
    readonly_fields = ('date',)

    def set_unconfirmed(self, request, queryset):
        queryset.update(status=0)
    set_unconfirmed.short_description = 'Изменить статус на "Не подтверждена"'

    def set_confirmed(self, request, queryset):
        queryset.update(status=1)
    set_confirmed.short_description = 'Изменить статус на "Подтверждена"'

    def set_cancelled(self, request, queryset):
        queryset.update(status=2)
    set_cancelled.short_description = 'Изменить статус на "Отменена"'

    def set_completed(self, request, queryset):
        queryset.update(status=3)
    set_completed.short_description = 'Изменить статус на "Выполнена"'

    def visit_number(self, obj):
        visits = Visit.objects.filter(phone=obj.phone).order_by('date')
        return visits.filter(date__lte=obj.date).count()
    visit_number.short_description = '№ визита'
    visit_number.admin_order_field = 'date'


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('display_photo', 'first_name', 'last_name', 'contact_info', 'completed_visits', 'confirmed_visits')
    list_display_links = ('display_photo', 'first_name', 'last_name', 'contact_info')
    search_fields = ('first_name', 'last_name', 'contact_info')
    list_filter = ('services',)
    readonly_fields = ('show_photo',)

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" />', obj.photo.url)
    display_photo.short_description = 'Фото (мини)'

    def show_photo(self, obj):
        return format_html('<img src="{}" width="200" />', obj.photo.url)
    show_photo.short_description = 'Фотография'

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'contact_info', 'show_photo', 'photo')
        }),
    )

    def completed_visits(self, obj):
        return Visit.objects.filter(master=obj, status=3).count()
    completed_visits.short_description = 'Оказано услуг'

    def confirmed_visits(self, obj):
        return Visit.objects.filter(master=obj, status=1).count()
    confirmed_visits.short_description = 'Ожидающие клиенты'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'all_visits')
    search_fields = ('name', 'price')
    list_filter = ('price',)
    list_editable = ('price',)

    def all_visits(self, obj):
        return Visit.objects.filter(services__name=obj, status=3).count()
    all_visits.short_description = 'Оказано услуг'
