from django import template
register=template.Library()

from sybing.models import *

@register.inclusion_tag('sidebar/cat.html')
def Cats():
    return {'cats':Category.objects.all(),}

@register.inclusion_tag('sidebar/tag.html')
def Tags():
    return {'tags':Tag.objects.all(),}

@register.inclusion_tag('sidebar/link.html')
def Links():
    return {'links':Link.objects.all(),}

@register.inclusion_tag('sidebar/recentblog.html')
def Titles():
    return {'titles':Blog.objects.all()[:6],}




