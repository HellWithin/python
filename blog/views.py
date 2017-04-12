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


def create_article(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect(reverse_lazy('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleForm()

    return render(request, 'blog/create_article.html', {'form': form})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'Object': article})


def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article_form = ArticleForm(request.POST or None, instance=article)
    if article_form.is_valid():
        article = Article.objects.get(pk=article_id)
        article_form.save()
        return HttpResponseRedirect(reverse_lazy('index'))


    return render(request, {'form': article_form}, 'blog/edit.html')
