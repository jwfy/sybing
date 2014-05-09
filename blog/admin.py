#!/usr/bin/python
# -*- coding: utf-8 -*-
from blog.models import Author, Blog, Tag, Picture, Category, Link
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


class PictureAdmin(admin.ModelAdmin):
    """docstring for PictureAdmin"""
    list_display = ('id', 'title', 'url', 'caption')
    search_fields = ('title',)
    date_hierarchy = 'time'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Blog, BlogAdmin)

