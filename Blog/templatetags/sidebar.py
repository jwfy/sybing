from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('sidebar/cat.html')
def Cats():
    return {'cats': Category.objects.all(), }


@register.inclusion_tag('sidebar/tag.html')
def Tags():
    return {'tags': Tag.objects.all(), }


@register.inclusion_tag('sidebar/link.html')
def Links():
    return {'links': Link.objects.all(), }


@register.inclusion_tag('sidebar/recentblog.html')
def Titles():
    return {'titles': Blog.objects.all()[:6], }


@register.inclusion_tag('sidebar/cat.html')
# about index html
def ICats():
    return {'cats': Category.objects.all()[:5], }


@register.inclusion_tag('sidebar/link.html')
def ILinks():
    return {'links': Link.objects.all(), }


@register.inclusion_tag('sidebar/recentblog.html')
def ITitles():
    return {'titles': Blog.objects.all()[:6], }
