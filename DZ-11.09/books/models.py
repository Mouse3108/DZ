from django.db import models


class Books(models.Model):
    title = models.TextField()
    publish_year = models.IntegerField()
    is_bestseller = models.BooleanField(default=False)
