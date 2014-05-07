# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.comments.models import Comment


class CustomComment(Comment):
    name = models.CharField(max_length=100, verbose_name=u'姓名')
    email = models.EmailField(max_length=100, verbose_name=u'邮箱')
    url = models.URLField(max_length=200, blank=True, verbose_name=u'站点')
    content = models.CharField(max_length=10000, verbose_name=u'评论')
    pk = models.IntegerField(verbose_name=u'文章ID')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')

    def __unicode__(self):
        return u'%s %s' % (self.email, self.pk)

    class Meta:

        ordering = ['-time']
        verbose_name_plural = u'评论'