#!/usr/bin/python
# -*- coding: utf-8 -*-
from sybing.models import Author, Blog, Tag, Picture, Category, Link, Music, MusicBox
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('id', 'caption', 'cat', 'count', 'publish_time')
    filter_horizontal = ('tags',)
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    #raw_id_fields = ('author',)  # 它是一个包含外键字段名称的元组，它包含的字段将被展现成`` 文本框`` ，而不再是`` 下拉框`` 。


class PictureAdmin(admin.ModelAdmin):
    """docstring for PictureAdmin"""
    list_display = ('id', 'title', 'url', 'caption')
    search_fields = ('title',)
    date_hierarchy = 'time'    


class MusicAdmin(admin.ModelAdmin):
    """主要是后台管理人员对音乐相关数据的管理"""
    list_display = ('name', 'author', 'cat', 'time')
    search_fields = ('name',)
    date_hierarchy = 'time'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(MusicBox)
admin.site.register(Music, MusicAdmin)

