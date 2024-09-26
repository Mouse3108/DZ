from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.db.models import F

menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog_catalog"},
    {"name": "Добавить пост", "alias": "add_post"},
    {"name": "О проекте", "alias": "about"}
]


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post.id)
    users = get_user_model().objects.all()
    context = {
        "post": post,
        "menu": menu,
        "page_alias": "blog_catalog",
        'comments': comments,
        'users': users
    }
    if request.method == "GET":
        post.views = F('views') + 1
        post.save()
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
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'menu': menu,
        'page_alias': 'main',
        'posts': posts,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'main.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'page_alias': 'about'
    }
    return render(request, 'about.html', context=context)


def blog_catalog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog_catalog'
    }
    return render(request, 'blog_app/blog.html', context=context)


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__slug=slug)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog_catalog',
        'tag': tag
    }
    return render(request, 'blog_app/blog_tag.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category__slug=slug)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
        'menu': menu,
        'page_alias': 'blog_catalog',
        'category': category
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
        if title and text and author:
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
                    post.category = Category.objects.get(id=category)
                else:
                    new_category = request.POST['new_category'].strip()
                    if new_category:
                        category = Category()
                        category.name = new_category
                        category.save()
                        post.category = category
                tags_list = request.POST.getlist('tag')
                new_tags = request.POST['new_tags']
                if new_tags:
                    new_tags_list = [tag.strip() for tag in new_tags.split(',')]
                    for new_tag in new_tags_list:
                        tag = Tag()
                        tag.name = new_tag
                        tag.save()
                        tags_list.append(tag.id)
                post.save()
                if tags_list:
                    tags = Tag.objects.filter(id__in=tags_list)
                    post.tags.set(tags)
                context.update({'message': 'Пост успешно добавлен!'})
                return render(request, 'blog_app/add_post.html', context)
            else:
                context.update({'message': 'Такой пост уже существует!'})
                return render(request, 'blog_app/add_post.html', context)
        else:
            context.update({'message': 'Поля <<Заголовок>>, <<Текст>> и <<Автор>> обязательно должны быть заполнены!'})
            return render(request, 'blog_app/add_post.html', context)
