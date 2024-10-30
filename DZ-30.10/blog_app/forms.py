from django import forms
from .models import *
from django.utils.text import slugify
from unidecode import unidecode


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['tags'] = ', '.join([tag.name for tag in self.instance.tags.all()])

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категорию",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Категория'
    )

    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите теги через запятую'}),
        label='Теги'
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'tags', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': 'id_text', 'required': False}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите теги через запятую'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'tags': 'Теги',
            'cover_image': 'Обложка',
        }

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            return [tag.strip().lower().replace(' ', '_') for tag in tags.split(',') if tag.strip()]
        return []

    def save(self, commit=True, author=None):
        instance = super().save(commit=False)
        if author:
            instance.author = author
        if commit:
            instance.save()
            self.save_tags(instance)
        return instance

    def save_tags(self, instance):
        instance.tags.clear()
        tag_names = self.cleaned_data.get('tags', [])
        if isinstance(tag_names, str):
            tag_names = [tag.strip().lower().replace(' ', '_') for tag in tag_names.split(',') if tag.strip()]
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
