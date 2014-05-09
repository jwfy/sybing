# -*- coding: utf-8 -*-
from music.models import Music, MusicBox
from django.contrib import admin


class MusicAdmin(admin.ModelAdmin):
    """主要是后台管理人员对音乐相关数据的管理"""
    list_display = ('name', 'author', 'cat', 'time')
    search_fields = ('name',)
    date_hierarchy = 'time'

admin.site.register(MusicBox)
admin.site.register(Music, MusicAdmin)
