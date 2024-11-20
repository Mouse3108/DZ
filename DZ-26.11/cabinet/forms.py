from django import forms
from core.models import *
from django.contrib.auth.forms import AuthenticationForm


class VisitUpdateForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'phone', 'master', 'services', 'status', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-info'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-info'}),
            'master': forms.Select(attrs={'class': 'form-control border-info'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control border-info'}),
            'status': forms.Select(attrs={'class': 'form-control border-info'}),
            'comment': forms.Textarea(attrs={'class': 'form-control border-info', 'rows': 3}),
        }


class AdminVisitCreateForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'phone', 'master', 'services', 'status', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-info'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-info'}),
            'master': forms.Select(attrs={'class': 'form-control border-info'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control border-info'}),
            'status': forms.Select(attrs={'class': 'form-control border-info'}),
            'comment': forms.Textarea(attrs={'class': 'form-control border-info', 'rows': 3}),
        }


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-info'
            field.widget.attrs['placeholder'] = field.label
