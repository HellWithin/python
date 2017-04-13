from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.article_edit, name='article_create'),
    url(r'^(?P<article_id>[0-9]+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^(?P<article_id>[0-9]+)/delete/$', views.article_delete, name='article_delete'),
    url(r'^search/$', views.article_search, name='article_search'),
]
