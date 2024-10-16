from django.contrib import admin
from .models import Post, Category, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_category', 'get_tags', 'status', 'published_date', 'updated_date', 'views',)
    list_filter = ('status',)
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}

    def get_category(self, obj):
        return obj.category.name if obj.category else "-"
    get_category.short_description = 'Категория'

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Теги'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'status', 'text')
    list_filter = ('status',)
    search_fields = ('author__username', 'text')
