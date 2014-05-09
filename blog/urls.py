# -*- coding: utf-8 -*-

from django.conf.urls import *
from blog.views import BlogListViewByPage, BlogDetailViewById, BlogListViewByCategory, BlogListViewByTag
from blog.views import BlogListViewBySearch


urlpatterns = patterns(('blog.views'),
    url (r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',
    url(r'^$', BlogListViewByPage.as_view(), name='blog'),
    url(r'^(?P<pk>\d+)/$', BlogDetailViewById.as_view(), name='blogdetail'),
    url(r'^cat/(?P<id>\d+)/$', BlogListViewByCategory.as_view(), name='blogbycat'),
    url(r'^tag/(?P<id>\d+)/$', BlogListViewByTag.as_view(), name='blogbytag'),
    url(r'^search/$', BlogListViewBySearch.as_view(), name='blogbysearch'),
)

