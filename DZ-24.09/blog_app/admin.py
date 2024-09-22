from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date', 'views')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
