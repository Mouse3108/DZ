from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик'),
    )
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    slug = models.SlugField(unique=True, verbose_name='Адрес страницы')
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', null=True, default=None, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name='posts', verbose_name='Теги')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    cover_image = models.ImageField(upload_to='post_covers/', blank=True, null=True, verbose_name='Картинка')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_by_slug", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        slug = slugify(unidecode(self.title))
        self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тег')
    slug = models.SlugField(unique=True, verbose_name='Адрес страницы')

    def save(self, *args, **kwargs):
        self.name = self.name.lower().replace(' ', '_')
        slug = slugify(unidecode(self.name))
        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'#{self.name}'

    def get_absolute_url(self):
        return reverse("post_by_tag", args=[str(self.slug)])

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Адрес страницы')

    def save(self, *args, **kwargs):
        self.name = self.name.lower().replace(' ', '_')
        slug = slugify(unidecode(self.name))
        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'*{self.name}'

    def get_absolute_url(self):
        return reverse("post_by_category", args=[str(self.slug)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Comment(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Опубликован'),
        ('rejected', 'Отклонен'),
        ('unchecked', 'На проверке'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unchecked', verbose_name='Статус')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Пост')

    def __str__(self):
        return f"Комментарий пользователя {self.author.username} к посту '{self.post.title}'"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
