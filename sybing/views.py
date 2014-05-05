# -*- coding: cp936 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from sybing.models import Tag, Category,  Author, Link, Blog, Music, Bug, BugSendMail
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models.expressions import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sybing.forms import BugForm
from django.core.mail import send_mail


class BlogListViewByPage(ListView):
    """ 主要是现实正常模式下的博客列表 """
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
    paginate_by = 6


class BlogDetailViewById(DetailView):
    """ 主要 是 显示一篇 完整的 博文内容 加入浏览数量 模块 """
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


class MusicListViewsById(ListView):
    """显示音乐界面，而且执行相关操作"""
    template_name = 'music.html'
    context_object_name = 'musics'
    queryset = Music.objects.all()


def about(request):
    """"显示关于页面的"""
    return render_to_response('about.html', context_instance=RequestContext(request))


def index(request):
    """"显示首页页面的"""
    return render_to_response('index.html', context_instance=RequestContext(request))


def nofound(self):
    """404页面"""
    return render_to_response('404.html')


def error(self):
    """500页面"""
    return render_to_response('500.html')


def BugPost(request):
    """bug 提交"""
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #  cd 就是即将存储的bug1的消息
            Burl = cd['url']
            Bname = cd['name']
            Bemail = cd['email']
            Bdescripe = cd['descripe']
            data = Bug(url=Burl, name=Bname, email=Bemail, descripe=Bdescripe)
            data.save()
            # 现在开始给管理员发送邮件,采用HTML的样式
            send_mail("BUG 提交", Bname + Bdescripe, 'jwfy0902@foxmail.com', ['986450042@qq.com'], fail_silently=True)
            return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))
    else:
        form = BugForm()
    return render_to_response('bug/bugpost.html', {'form': form}, context_instance=RequestContext(request))


def BugSuccess(request):
    """提交bug转跳页面"""
    return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))