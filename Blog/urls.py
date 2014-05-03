# -*- coding: cp936 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

#�������ڲ��Ե�ʱ��ֱ�ӵ����sybing�е�views��ͼ
#from sybing import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # ͬ�����˵����ƥ���
    #(r'^sybing/bloglist',views.blog_list),

)
#  �������ģ�黯�ĺܺõ�һ�����ӣ������ǵ�app�����ʱ�򣬵��ú����׳������⣬��ͺܷ�����
urlpatterns += patterns((''),
    (r'^sybing/',include('sybing.urls')),      
)

#  �����ڵ�����һ���ʱ�������
if settings.DEBUG is False:
    urlpatterns += patterns('',

        url ( r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT}),

   )



