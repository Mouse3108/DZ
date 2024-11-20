from django import forms
from .models import *
import re


class VisitModelForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'phone', 'comment', 'master', 'services']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Комментарий', 'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                widget_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{widget_classes} is-invalid'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        phone_pattern = r'^(\+7|8)\d{10}$'
        if not re.match(phone_pattern, phone):
            raise forms.ValidationError('Номер телефона должен начинаться с +7 или с 8 и содержать 10 цифр после кода страны.')

        return phone

    def clean(self):
        cleaned_data = super().clean()
        master = cleaned_data.get('master')
        selected_services = cleaned_data.get('services')

        if master and selected_services:
            master_services = set(master.services.values_list('name', flat=True).distinct())
            
            selected_services_set = set(service.name for service in selected_services)

            master_services = {service.lower() for service in master_services}
            selected_services_set = {service.lower() for service in selected_services_set}
            
            if not selected_services_set.issubset(master_services):
                unsupported_services = selected_services_set - master_services
                unsupported_services_str = ', '.join(unsupported_services)
                self.add_error('services', f"Мастер {master.first_name} {master.last_name} не предоставляет следующие услуги: {unsupported_services_str}.")

        return cleaned_data
