# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.comments.models import Comment
# from django.contrib.comments.managers import CommentManager
# from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    """docstring for Tags"""
    name = models.CharField(max_length=100, verbose_name=u'标签')

    def __unicode__(self):

        return u'%s' % (self.name,)

    class Meta:
        verbose_name_plural = u'标签'


class Category(models.Model):
    """目录"""
    name = models.CharField(max_length=100, verbose_name=u'目录')

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name_plural = u'目录'


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30, verbose_name=u'帐户名')
    email = models.EmailField(verbose_name=u'邮箱')
    website = models.URLField(blank=True, verbose_name=u'个人站点')

    def __unicode__(self):
        return u'%s' % (self.name,)

    class Meta:
        verbose_name_plural = u'作者'


class Link(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'标题')
    url = models.URLField(max_length=500, verbose_name=u'地址')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.url)

    class Meta:
        verbose_name_plural = u'链接'


class Blog(models.Model):
    """docstring for blog"""
    caption = models.CharField(max_length=50, verbose_name=u"标题")
    author = models.ForeignKey(Author, verbose_name=u"作者")
    cat = models.ForeignKey(Category, verbose_name=u'目录')
    tags = models.ManyToManyField(Tag, verbose_name=u'标签')
    content = models.TextField(verbose_name=u"内容")
    count = models.IntegerField(verbose_name=u'浏览次数', default=0)
    commit_count = models.IntegerField(verbose_name=u'评论数', default=0)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.caption,)

    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = u'博文'


class Picture(models.Model):
    """ 主要是中间的大图滚轮和以后的相册使用"""
    url = models.CharField(max_length=500, verbose_name=u"地址")
    title = models.CharField(max_length=50, verbose_name=u"标题", blank=True, null=True)
    caption = models.CharField(max_length=200, verbose_name=u"描述", blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-time']
        verbose_name_plural = u'图片'


# class BlogCommentsManager(CommentManager):
#     """自定义博客评论模块的相关操作"""
#     def get_blog_comment(self, blog):
#         """过滤出具体博客的评论"""
#         blog_type = ContentType.objects.get_for_model(blog)
#         return Comment.objects.filter(content_type=blog_type, object_pk=blog.pk)
#
#
# class BlogComments(Comment):
#     """继承comment的相关方法"""
#     objects = BlogCommentsManager()