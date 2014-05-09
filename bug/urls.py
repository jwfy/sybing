# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns('',
    url(r'^$', 'bug.views.BugPost', name='bug'),
    url(r'^success/$', 'bug.views.BugSuccess', name='bugsuccess'),
)