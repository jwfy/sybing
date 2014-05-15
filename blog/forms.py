# # -*-coding:utf-8 -*-
#
# from django import forms
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.comments.models import Comment
# from blog.models import BlogComments
#
#
# class BlogCommentsForm(forms.ModelForm):
#
#         # def __init__(self, *args, **kwargs):
#         #     super(BlogCommentsForm, self).__init__(*args, **kwargs)
#         #
#         #     self.fields['user_name'].required = True
#         #     self.fields['user_name'].error_messages = {'required': u'怎么称呼您？'}
#         #
#         #     self.fields['user_email'].required = True
#         #     self.fields['user_email'].error_messages = {'required': u'请填写您的邮箱，仅为了保持联系！',
#         #                                                 'invalid': u'邮箱格式错误'}
#         #     self.fields['user_url'].error_messages = {'invalid': u'个人站点格式错误'}
#         #     self.fields['comment'].error_messages = {'required': u'请输入您的留言'}
#
#         # def save(self, blog, ip, site, commit=True):
#         #     obj = super(BlogCommentsForm, self).save(commit=False)
#         #     obj.ip_address = ip
#         #     obj.site = site
#         #     obj.content_type = ContentType.objects.get_for_model(blog)
#         #     obj.object_pk = blog.pk
#         #
#         #     if commit:
#         #         obj.save()
#         #     return obj
#
#         class Meta:
#             model = BlogComments
#             fields = ['user_name', 'user_email', 'user_url', 'comment']
