from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog"},
    {"name": "О проекте", "alias": "about"},
]


def post_by_slug(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        "post": post,
        "menu": menu,
        "page_alias": "blog"
    }
    return render(request, 'blog_app/post_detail.html', context=context, status=200)
    

def main(request):
    posts = Post.objects.all()
    context = {
        'menu': menu,
        'page_alias': 'main',
        'posts': posts
    }
    return render(request, 'main.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'page_alias': 'about'
    }
    return render(request, 'about.html', context=context)


def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog'
    }
    return render(request, 'blog_app/blog.html', context=context)
