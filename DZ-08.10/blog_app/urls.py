from django.urls import path
from .views import *


urlpatterns = [
    path("", blog_catalog, name="blog_catalog"),
    path('<slug:slug>/view', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('tag/<slug:slug>/', tag_detail, name='tag_detail'),
    path('add/', add_post, name='add_post'),
]
