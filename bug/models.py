# -*- coding: utf-8 -*-
from django.db import models


class Bug(models.Model):
    """bug提交的相关数据库"""
    url = models.CharField(max_length=100, verbose_name=u'地址')
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    email = models.EmailField(max_length=100, verbose_name=u'邮箱地址')
    descripe = models.CharField(max_length=100, verbose_name=u'描述')
    define = models.BooleanField(blank=True, verbose_name=u'确认回复')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'提交时间')
    enable_sendmail = models.BooleanField(default=True, verbose_name=u'邮件接收')

    def __unicode__(self):
        return u'%s  %s' % (self.name, self.descripe)

    class Meta:

        verbose_name_plural = u'问题提交'