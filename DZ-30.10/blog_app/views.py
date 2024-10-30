from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F, Q
from .models import *
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import PostForm
import json
from .templatetags.md_to_html import markdown_to_html
from django.utils.http import urlencode
from urllib.parse import unquote


menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog_catalog"},
    {"name": "Добавить пост", "alias": "add_post"},
    {"name": "О проекте", "alias": "about"}
]


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.prefetch_related('tags').select_related('author').select_related('category'), slug=slug)
    if f'post_{post.id}_viewed' not in request.session:
        Post.objects.filter(slug=slug).update(views=F('views') + 1)
        request.session[f'post_{post.id}_viewed'] = True
    comments = Comment.objects.select_related('author').select_related('post').filter(post=post.id).filter(status='approved')
    user = request.user
    context = {
        "post": post,
        "menu": menu,
        "page_alias": "blog_catalog",
        'comments': comments
    }
    if request.method == "GET":
        return render(request, 'blog_app/post_detail.html', context=context, status=200)
    elif request.method == "POST":
        text = request.POST['text']
        author = user
        if not request.user.is_authenticated:
            messages.error(request, 'Только зарегистрированные пользователи могут оставлять комментарии!')
            return render(request, 'blog_app/post_detail.html', context)
        if text:
            comment = Comment()
            comment.text = text
            comment.author = author
            comment.post = post
            comment.save()
            messages.success(request, 'Комментарий добавлен и находится на модерации!')
            return render(request, 'blog_app/post_detail.html', context)
        else:
            messages.error(request, 'Комментарий не может быть пустым!')
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


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not request.user.is_authenticated:
            messages.error(request, 'Только зарегистрированные пользователи могут добавлять посты!')
            return redirect('add_post')
        if form.is_valid():
            post = form.save(commit=True, author=request.user)
            messages.success(request, 'Пост успешно создан и находится на модерации!')
            return redirect('add_post')
    else:
        form = PostForm()
    return render(request, 'blog_app/add_post.html',
                  {'form': form,
                           'menu': menu,
                           'operation': 'Добавить пост'})


def update_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно обновлен!')
            return redirect('update_post', post_slug=post_slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/add_post.html',
                  {'form': form,
                           'menu': menu,
                           'operation': 'Редактировать пост'})
