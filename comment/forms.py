# -*- coding: utf-8 -*-
from django import forms
from django.contrib.comments.forms import CommentForm
from comment.models import CustomComment

url_error = {
    'required': '问题网址是必填项',
    'invalid': '请输入一个有效值'
}
name_error = {
    'required': '请留下您的姓名',
    'invalid': '请输入一个有效值'
}
email_error = {
    'required': '请留下您的邮箱地址',
    'invalid': '请输入一个有效的地址,例如 zhangsan@qq.com'
}
content_error = {
    'required': '问题描述必须填写',
    'invalid': '请输入一个有效值'
}


class CustomCommentForm(CommentForm):
    name = forms.CharField(error_messages=name_error, label=u'姓名', max_length=100, widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "您的姓名"}))
    email = forms.EmailField(error_messages=email_error, label=u'邮箱', max_length=100, widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "您的邮箱地址"}))
    url = forms.URLField(error_messages=url_error, label=u'个人站点', max_length=200, required=False, widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "您的个人站点"}))
    content = forms.CharField(error_messages=content_error, label=u'评论', max_length=10000,  widget=forms.Textarea(attrs={'css': "self-input", "placeholder": "请输入您发现的问题描述"}))
    pk = forms.IntegerField(widget=forms.HiddenInput())   #默认文章的ID，隐藏项目

    def get_comment_model(self):
        return CustomComment

    def get_comment_create_data(self):
        data = super(CustomCommentForm, self).get_comment_create_data()
        data['name'] = self.cleaned_data['name']
        data['email'] = self.cleaned_data['email']
        data['url'] = self.cleaned_data['url']
        data['content'] = self.cleaned_data['content']
        data['pk'] = self.cleaned_data['pk']
        return data