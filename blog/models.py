# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    change_date = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
