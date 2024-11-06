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


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return (Post.objects.prefetch_related('tags').
                select_related('author', 'category'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'blog_catalog'
        context['comments'] = (Comment.objects.select_related('author').
        select_related('post').filter(
            post=self.object.id,
            status='approved'
        ))
        context['users'] = get_user_model().objects.all()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if f'post_{self.object.id}_viewed' not in request.session:
            (Post.objects.filter(slug=self.object.slug).
             update(views=F('views') + 1))
            request.session[f'post_{self.object.id}_viewed'] = True
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        text = request.POST.get('text')
        author_id = request.POST.get('author')
        if text and author_id:
            comment = Comment(
                text=text,
                author=get_user_model().objects.get(id=author_id),
                post=self.object
            )
            comment.save()
            messages.success(request, 'Комментарий добавлен! Он будет опубликован после подтверждения администратора.')
        else:
            messages.error(request, 'Поля автор и комментарий обязательно должны быть заполнены!')
        return self.render_to_response(context)


class MainView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.prefetch_related('tags').select_related('author', 'category').filter(status="published")
        for post in queryset:
            post.short_text = post.text.split('<!--more-->')[0]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'main'
        context['comments'] = Comment.objects.select_related('author').select_related('post').filter(status='approved')
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'about'
        context['dz'] = DZ.objects.last()
        return context


class BlogCatalogView(ListView):
    model = Post
    template_name = 'blog_app/blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = (Post.objects.prefetch_related('tags').
                    select_related('author', 'category').
                    filter(status="published"))
        search_query = unquote(self.request.GET.get("search", ""))
        search_category = self.request.GET.get("search_category")
        search_tag = self.request.GET.get("search_tag")
        if search_query:
            query = Q(title__icontains=search_query) | Q(text__icontains=search_query)
            if search_category:
                query |= Q(category__name__icontains=search_query)
            if search_tag:
                query |= Q(tags__name__icontains=search_query)
            queryset = queryset.filter(query)
        queryset = queryset.distinct().order_by("-published_date")
        for post in queryset:
            post.short_text = post.text.split('<!--more-->')[0]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'blog_catalog'
        context['comments'] = (Comment.objects.select_related('author').
                               select_related('post').
                               filter(status='approved'))
        search_query = unquote(self.request.GET.get("search", ""))
        search_category = self.request.GET.get("search_category")
        search_tag = self.request.GET.get("search_tag")
        context['search_query'] = urlencode({
            'search': search_query,
            'search_category': 'on' if search_category else '',
            'search_tag': 'on' if search_tag else ''
        })
        return context


class TagDetailView(ListView):
    model = Post
    template_name = 'blog_app/blog_tag.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        queryset = Post.objects.prefetch_related('tags').select_related('author', 'category').filter(
            status="published",
            tags__slug=self.kwargs['slug']
        )
        for post in queryset:
            post.short_text = post.text.split('<!--more-->')[0]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'blog_catalog'
        context['tag'] = self.tag
        context['comments'] = (Comment.objects.select_related('author').
                               select_related('post').
                               filter(status='approved'))
        return context


class CategoryDetailView(ListView):
    model = Post
    template_name = 'blog_app/blog_category.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Post.objects.prefetch_related('tags').select_related('author', 'category').filter(
            status="published",
            category__slug=self.kwargs['slug']
        )
        for post in queryset:
            post.short_text = post.text.split('<!--more-->')[0]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['page_alias'] = 'blog_catalog'
        context['category'] = self.category
        context['comments'] = Comment.objects.select_related('author').select_related('post').filter(status='approved')
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Пост успешно создан и находится на модерации!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['operation'] = 'Добавить пост'
        context['page_alias'] = 'add_post'
        return context


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_app/add_post.html'
    slug_url_kwarg = 'post_slug'

    def get_success_url(self):
        return reverse('update_post', kwargs={'post_slug': self.object.slug})

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно обновлен!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['operation'] = 'Редактировать пост'
        return context
