from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('all_articles/', views.all_article, name='all_article'),
    path('add_article/', views.add_article, name='add_article'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]

