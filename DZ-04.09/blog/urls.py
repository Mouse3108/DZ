from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_catalog),
    path('category/', views.category_list),
    path('category/<int:category_id>/', views.category_detail),
]

