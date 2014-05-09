# -*- coding: cp936 -*-
from bug.models import Bug
from bug.forms import BugForm


from sybing.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response


def BugPost(request):
    """bug 提交"""
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #  cd 就是即将存储的bug1的消息
            Burl = cd['url']
            Bname = cd['name']
            Bemail = cd['email']
            Bdescripe = cd['descripe']
            data = Bug(url=Burl, name=Bname, email=Bemail, descripe=Bdescripe)
            data.save()
            #   这句话是直接利用send发送邮件的
            # send_mail("BUG submit", "Hello World", EMAIL_HOST_USER, [Bemail], fail_silently=True)
            #  采用HTML 模板发送邮件
            subject = u'Bug 提交'
            from_email = EMAIL_HOST_USER    #发送邮件的账户
            to_email = ['986450042@qq.com', 'sybing@live.cn']        #同时给管理员和发送bug的用户发送邮件
            text = get_template('email/BugSendAdmin.txt')
            html = get_template('email/BugSendAdmin.html')
            cc = Context({'name': Bname, 'email': Bemail, 'contain': Bdescripe, 'url': Burl})
            text_content = text.render(cc)
            html_content = html.render(cc)
            #
            # #  现在开始发送邮件实体
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))
    else:
        form = BugForm()
    return render_to_response('bug/bugpost.html', {'form': form}, context_instance=RequestContext(request))


def BugSuccess(request):
    """提交bug转跳页面"""
    return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))