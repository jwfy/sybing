# -*- coding: utf-8 -*-
from django.db import models


class MusicBox(models.Model):
    """这个是音乐目录的分类"""
    title = models.CharField(max_length=100, verbose_name=u"目录")
    picurl = models.URLField(max_length=500, verbose_name=u"封面地址")
    time = models.DateTimeField(auto_now_add=True, verbose_name=u"上传时间")

    def __unicode__(self):
        return u'%s' % (self.title,)

    class Meta:

        ordering = ['-time']
        verbose_name_plural = u'音乐目录'


class Music(models.Model):
    """这是在“音乐页面”的主要的歌曲信息"""
    url = models.CharField(max_length=500, verbose_name=u"歌曲地址")
    #url = models.FileField(upload_to="music",verbose_name=u"歌曲地址")
    name = models.CharField(max_length=100, verbose_name=u"歌曲名称")
    author = models.CharField(max_length=100, verbose_name=u"歌曲作者")
    picture = models.URLField(blank=True, max_length=500, verbose_name=u"作者头像")
    lrc = models.URLField(blank=True, max_length=500, verbose_name=u"歌词地址")
    cat = models.ForeignKey(MusicBox, verbose_name=u'歌曲目录')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u"上传时间")

    def __unicode__(self):
        return u'%s-%s' % (self.name, self.author,)

    class Meta:

        ordering = ['-time']
        verbose_name_plural = u'音乐'

