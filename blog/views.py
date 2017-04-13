# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import forms
import models


def index(request):
    form = forms.Search(request.GET or None)
    articles_list = models.Article.objects.order_by('-pub_date')

    if form.is_valid():
        keyword = form.cleaned_data['keyword']
        articles_list = articles_list.filter(title__icontains=keyword)

    paginator = Paginator(articles_list, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'articles': articles, 'form': form})


def article_edit(request, article_id=None):
    article = None
    if article_id:
        article = get_object_or_404(models.Article, pk=article_id)
        form = forms.Article(request.POST or None, instance=article)
    else:
        form = forms.Article(request.POST or None, instance=article)

    if form.is_valid():
        article = form.save()
        if request.user.is_authenticated:
            article.user = request.user
            article.save()
        return HttpResponseRedirect(reverse_lazy('index'))
    return render(request, 'blog/edit.html', {'form': form})


def article_detail(request, article_id):
    obj = get_object_or_404(models.Article, pk=article_id)
    return render(request, 'blog/article.html', {'object': obj})


def article_search(request, keyword):
    return render(request, 'blog/index.html', {'articles': articles, })


def article_delete(request, article_id=None):
    article = get_object_or_404(models.Article, pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse_lazy('index'))
