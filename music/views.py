# -*- coding: utf-8 -*-

from django.views.generic import ListView
from music.models import Music


class MusicListViewsById(ListView):
    """显示音乐界面，而且执行相关操作"""
    template_name = 'music.html'
    context_object_name = 'musics'
    queryset = Music.objects.all()