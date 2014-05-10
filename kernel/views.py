# -*-coding:utf-8 -*-
from django.conf import settings


class GetBlogCommentsIP(object):
    """用来获取客户端的ip的"""
    allowed_ips = getattr(settings, 'ALLOWED_IPS', [])

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def is_access_allowed(self, request):
        return self.get_client_ip(request) in self.allowed_ips