# -*- coding: cp936 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from single.views import Index, About


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
                        url(r'^blog/', include('blog.urls')),
                        url(r'^music/', include('music.urls')),
                        url(r'^bug/', include('bug.urls')),
                        url(r'^$', Index.as_view(), name='index'),
                        url(r'^about', About.as_view(), name='about'),
                        )
#  这是在调试这一块的时候的设置
if settings.DEBUG is False:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )



