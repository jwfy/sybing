# -*-coding:utf-8 -*-

from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'