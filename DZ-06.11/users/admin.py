from django.contrib import admin
from .models import *


@admin.register(User)
class DZAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'is_superuser', 'date_joined', 'email', 'date_birth')
