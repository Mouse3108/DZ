from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    photo = models.ImageField(upload_to='users/images/%Y/%m/%d/', blank=True, null=True, verbose_name='Фотография')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    github_id = models.CharField(max_length=255, blank=True, null=True)
    vk_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'self.username'
