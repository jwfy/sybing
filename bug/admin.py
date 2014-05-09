#!/usr/bin/python
# -*- coding: utf-8 -*-
from bug.models import Bug
from django.contrib import admin


class BugAdmin(admin.ModelAdmin):
    """后台bug描述管理提交"""
    list_display = ('name', 'email', 'descripe', 'url', 'define')
    search_fields = ('descripe',)
    date_hierarchy = 'time'


admin.site.register(Bug, BugAdmin)