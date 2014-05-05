# -*- coding: utf-8 -*-

from django.conf.urls import *
from sybing.views import BlogListViewByPage, BlogDetailViewById, BlogListViewByCategory, BlogListViewByTag
from sybing.views import BlogListViewBySearch, MusicListViewsById


urlpatterns = patterns(('sybing.views'),
    url (r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',
    url(r'^blog/$', BlogListViewByPage.as_view(), name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', BlogDetailViewById.as_view(), name='blogdetail'),
    url(r'^blog/cat/(?P<id>\d+)/$', BlogListViewByCategory.as_view(), name='blogbycat'),
    url(r'^blog/tag/(?P<id>\d+)/$', BlogListViewByTag.as_view(), name='blogbytag'),
    url(r'^blog/search/$', BlogListViewBySearch.as_view(), name='blogbysearch'),
    url(r'^music/$', MusicListViewsById.as_view(), name='music'),
    url(r'^about/$', 'sybing.views.about', name='about'),
    url(r'^bug/post/$', 'sybing.views.BugPost', name='bug'),
    url(r'^bug/post/success/$','sybing.views.BugSuccess', name='bugsuccess'),
    url(r'^$', 'sybing.views.index', name='index'),
)

