# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from models import Article
from forms import ArticleForm


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_articles_list': latest_articles_list}
    return render(request, 'blog/index.html', context)


def article_edit(request, article_id=None):
    article = None
    if article_id:
        article = get_object_or_404(Article, pk=article_id)

    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        article = Article.objects.get(pk=article_id)
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

