from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True, default=list)
    views = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_by_slug", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        slug = slugify(unidecode(self.title))
        self.slug = slug
        super().save(*args, **kwargs)
