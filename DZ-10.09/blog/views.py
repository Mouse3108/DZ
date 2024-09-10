from django.shortcuts import render, HttpResponse
from .articles import articles

context = {
    'articles': articles
}


def main_page(request):
    if len(articles) > 5:
        new_articles = {
          'articles': articles[-5:][::-1]
        }
    return render(request, 'all_article.html', context=new_articles)


def article_detail(request, article_id):
    article = [article for article in articles if article['id'] == article_id]
    if not article:
        return HttpResponse('404 - Статья не найдена', status=404)
    else:
        return render(request, 'article_detail.html', context=article[0], status=200)


def all_article(request):
    return render(request, 'all_article.html', context=context)


def add_article(request):
    return render(request, 'add_article.html')
