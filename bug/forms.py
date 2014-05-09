__author__ = 'syb'
# -*- coding: utf-8 -*-
from django import forms

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
descripe_error = {
    'required': '问题描述必须填写',
    'invalid': '请输入一个有效值'
}


class BugForm(forms.Form):
    """bug提交的相关数据表单"""
    url = forms.CharField(error_messages=url_error, max_length=100, required=True, label='网址', widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "请输入您发现缺陷的网址"}))
    name = forms.CharField(error_messages=name_error, max_length=20, required=True, label='姓名', widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "请输入您的姓名"}))
    email = forms.EmailField(error_messages=email_error, max_length=100, required=True, label='邮箱', widget=forms.TextInput(attrs={'css': "self-input", "placeholder": "请输入您的邮箱（确保以后联系）"}))
    descripe = forms.CharField(error_messages=descripe_error, max_length=100, required=True, label='描述', widget=forms.Textarea(attrs={'css': "self-input", "placeholder": "请输入您发现的问题描述"}))




