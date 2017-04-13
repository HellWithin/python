# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import ModelForm, Textarea
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import Article
from forms import ArticleView, ArticleEdit

def index(request):
    articles_list = Article.objects.order_by('-pub_date')
    paginator = Paginator(articles_list, 2)

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'articles': articles})

def article_edit(request, article_id=None):
    article = None
    if article_id:
        article = get_object_or_404(Article, pk=article_id)
        form = ArticleEdit(request.POST or None, instance=article)
    else:
        form = ArticleView(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('index'))

    return render(request, 'blog/edit.html', {'form': form})


def article_detail(request, article_id):
    obj = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'object': obj})

def article_delete(request, article_id=None):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse_lazy('index'))

