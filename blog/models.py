# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Article(models.Model):
    change_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.title

