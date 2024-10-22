from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from django.db.models import F
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .templatetags.md_to_html import markdown_to_html
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import urlencode
from urllib.parse import unquote

menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog_catalog"},
    {"name": "Добавить пост", "alias": "add_post"},
    {"name": "О проекте", "alias": "about"}
]


def post_detail(request, slug):
    Post.objects.filter(slug=slug).update(views=F('views') + 1)
    post = get_object_or_404(Post.objects.prefetch_related('tags').select_related('author').select_related('category'), slug=slug)
    comments = Comment.objects.select_related('author').select_related('post').filter(post=post.id).filter(status='approved')
    users = get_user_model().objects.all()
    context = {
        "post": post,
        "menu": menu,
        "page_alias": "blog_catalog",
        'comments': comments,
        'users': users
    }
    if request.method == "GET":
        return render(request, 'blog_app/post_detail.html', context=context, status=200)
    elif request.method == "POST":
        text = request.POST['text']
        author = request.POST['author']
        if text and author:
            comment = Comment()
            comment.text = text
            comment.author = get_user_model().objects.get(id=author)
            comment.post = post
            comment.save()
            context.update(
                {'message': 'Комментарий добавлен! Он будет опубликован после подтверждения администратора.'})
            return render(request, 'blog_app/post_detail.html', context)
        else:
            context.update(
                {'message': 'Поля автор и комментарий обязательно должны быть заполнены!'})
            return render(request, 'blog_app/post_detail.html', context)


def main(request):
    posts = Post.objects.prefetch_related('tags').select_related('author').select_related('category').filter(status="published")
    comments = Comment.objects.select_related('author').select_related('post').filter(status='approved')
    for post in posts:
        post.short_text = post.text.split('<!--more-->')[0]
    context = {
        'menu': menu,
        'page_alias': 'main',
        'posts': posts,
        'comments': comments
    }
    return render(request, 'main.html', context=context)


def about(request):
    dz = DZ.objects.last()
    context = {
        'menu': menu,
        'page_alias': 'about',
        'dz': dz
    }
    return render(request, 'about.html', context=context)


def blog_catalog(request):
    search_query = unquote(request.GET.get("search", ""))
    search_category = request.GET.get("search_category")
    search_tag = request.GET.get("search_tag")
    page_number = request.GET.get('page', 1)
    posts = Post.objects.prefetch_related('tags').select_related('author', 'category').filter(status="published")
    comments = Comment.objects.select_related('author').select_related('post').filter(status='approved')
    if search_query:
        query = Q(title__icontains=search_query) | Q(text__icontains=search_query)
        if search_category:
            query |= Q(category__name__icontains=search_query)
        if search_tag:
            query |= Q(tags__name__icontains=search_query)
        posts = posts.filter(query)

    posts = posts.distinct().order_by("-published_date")
    for post in posts:
        post.short_text = post.text.split('<!--more-->')[0]
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'menu': menu,
        'page_alias': 'blog_catalog',
        'comments': comments,
        'search_query': urlencode(
            {'search': search_query,
             'search_category': 'on' if search_category else '',
             'search_tag': 'on' if search_tag else ''})
    }
    return render(request, 'blog_app/blog.html', context=context)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = (Post.objects.prefetch_related('tags').select_related('author').select_related('category').
             filter(status="published").filter(tags__slug=slug))
    comments = Comment.objects.select_related('author').select_related('post').filter(status='approved')
    for post in posts:
        post.short_text = post.text.split('<!--more-->')[0]
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog_catalog',
        'tag': tag,
        'comments': comments
    }
    return render(request, 'blog_app/blog_tag.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = (Post.objects.prefetch_related('tags').select_related('author').select_related('category').
             filter(status="published").filter(category__slug=slug))
    comments = Comment.objects.select_related('author').select_related('post').filter(status='approved')
    for post in posts:
        post.short_text = post.text.split('<!--more-->')[0]
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog_catalog',
        'category': category,
        'comments': comments
    }
    return render(request, 'blog_app/blog_category.html', context=context)


def add_post(request):
    users = get_user_model().objects.all()
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    context = {
        'menu': menu,
        'page_alias': 'add_post',
        'users': users,
        'categories': categories,
        'tags': all_tags
    }
    if request.method == "GET":
        return render(request, 'blog_app/add_post.html', context=context)
    elif request.method == "POST":
        title = request.POST['title'].strip()
        text = request.POST['text'].strip()
        author = request.POST['author']
        if title and text and author != 'Выберите пользователя':
            if not Post.objects.filter(title=title).exists():
                post = Post()
                post.title = title
                post.text = text
                post.author = get_user_model().objects.get(id=author)
                cover_image = request.FILES.get('cover_image')
                if cover_image:
                    post.cover_image = cover_image
                category = request.POST['category']
                if category:
                    category_name = category.strip().lower().replace(' ', '_')
                    category, created = Category.objects.get_or_create(name=category_name)
                    post.category = category
                post.save()
                tags = request.POST['tags']
                tag_list = [tag.strip().lower().replace(' ', '_') for tag in tags.split(',') if tag.strip()]
                for tag_name in tag_list:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
                context.update({'message': 'Пост успешно добавлен!'})
                return render(request, 'blog_app/add_post.html', context)
            else:
                context.update({'message': 'Такой пост уже существует!'})
                return render(request, 'blog_app/add_post.html', context)
        else:
            context.update({'message': 'Поля <<Заголовок>>, <<Текст>> и <<Автор>> обязательно должны быть заполнены!'})
            return render(request, 'blog_app/add_post.html', context)
