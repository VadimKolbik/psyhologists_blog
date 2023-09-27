from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class PostHome(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['title'] = 'Главная страница'
        context['cats'] = cats
        return context

class PostCategory(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'cat_slug'

    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['title'] = 'Главная страница'
        context['cats'] = cats
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['cat_selected'] = cat.pk
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug' #т.к. в url маршруте указана наименование переменной slug "post_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['title'] = context['post']
        context['cats'] = cats
        return context
