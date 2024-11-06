from django.urls import path
from .views import *


urlpatterns = [
    path("", BlogCatalogView.as_view(), name="blog_catalog"),
    path('<slug:slug>/view', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name='tag_detail'),
    path('add/', AddPostView.as_view(), name='add_post'),
    path("update_post/<slug:post_slug>/", UpdatePostView.as_view(), name="update_post"),
]
