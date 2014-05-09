# -*- coding: utf-8 -*-

from django.conf.urls import *
from music.views import MusicListViewsById

urlpatterns = patterns('',
    url(r'^$', MusicListViewsById.as_view(), name='music'),
)
