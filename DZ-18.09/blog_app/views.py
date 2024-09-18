from django.shortcuts import render, HttpResponse
from .dataset import dataset
from django.core.paginator import Paginator

menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog"},
    {"name": "О проекте", "alias": "about"},
]


def post_by_slug(request, post_slug):
    post = [post for post in dataset if post['slug'] == post_slug]
    if not post:
        return HttpResponse('404 - Пост не найден', status=404)
    else:
        context = post[0]
        context['menu'] = menu
        context['page_alias'] = 'blog'
        return render(request, 'blog_app/post_detail.html', context=context, status=200)
    

def main(request):
    context = {
        'menu': menu,
        'page_alias': 'main',
        'posts': [post for post in dataset]
    }
    return render(request, 'main.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'page_alias': 'about'
    }
    return render(request, 'about.html', context=context)


def blog(request):
    posts = [post for post in dataset]
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog'
    }
    return render(request, 'blog_app/blog.html', context=context)
