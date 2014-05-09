# -*- coding: cp936 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models.expressions import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogListViewByPage(ListView):
    """ Ö÷ҪÊÇÏÖʵÕý³£ģʽÏµĲ©¿ÍÁбí """
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
    paginate_by = 6


class BlogDetailViewById(DetailView):
    """ Ö÷Ҫ ÊÇ ÏÔʾһƪ ÍêÕûµÄ ²©ÎÄÄÚÈÝ ¼ÓÈëä¯ÀÀÊý ģ¿é """
    queryset = Blog.objects.all()
    context_object_name = 'article'
    template_name = 'blog/blog_detail.html'

    def get_object(self):
        object = super(BlogDetailViewById, self).get_object()
        object.count += 1
        object.save()
        return object


class BlogListViewByCategory(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(cat=self.kwargs['id'])


class BlogListViewByTag(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(tags=self.kwargs['id'])


class BlogListViewBySearch(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Blog.objects.filter(Q(caption__icontains=q) | Q(content__icontains=q)).distinct()


def about(request):
    """"ÏÔʾ¹ØÓÚҳÃæµÄ"""
    return render_to_response('about.html', context_instance=RequestContext(request))


def index(request):
    """"ÏÔʾÊ×ҳҳÃæµÄ"""
    return render_to_response('index.html', context_instance=RequestContext(request))


def nofound(self):
    """404ҳÃæ"""
    return render_to_response('404.html')


def error(self):
    """500ҳÃæ"""
    return render_to_response('500.html')