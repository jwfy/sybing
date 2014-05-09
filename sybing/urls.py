# -*- coding: cp936 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

#这里是在测试的时候直接导入的sybing中的views视图

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#  这里就是模块化的很好的一个例子，当我们的app过多的时候，调用很容易出现问题，这就很方便了
urlpatterns += patterns((''),
    (r'^blog/', include('blog.urls')),
    (r'^music/', include('music.urls')),
    (r'^bug/', include('bug.urls'))
)

#  这是在调试这一块的时候的设置
if settings.DEBUG is False:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
   )



