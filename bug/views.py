# -*- coding: cp936 -*-
from bug.models import Bug
from bug.forms import BugForm


from sybing.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response


def BugPost(request):
    """bug �ύ"""
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #  cd ���Ǽ����洢��bug1����Ϣ
            Burl = cd['url']
            Bname = cd['name']
            Bemail = cd['email']
            Bdescripe = cd['descripe']
            data = Bug(url=Burl, name=Bname, email=Bemail, descripe=Bdescripe)
            data.save()
            #   ��仰��ֱ������send�����ʼ���
            # send_mail("BUG submit", "Hello World", EMAIL_HOST_USER, [Bemail], fail_silently=True)
            #  ����HTML ģ�巢���ʼ�
            subject = u'Bug �ύ'
            from_email = EMAIL_HOST_USER    #�����ʼ����˻�
            to_email = ['986450042@qq.com', 'sybing@live.cn']        #ͬʱ������Ա�ͷ���bug���û������ʼ�
            text = get_template('email/BugSendAdmin.txt')
            html = get_template('email/BugSendAdmin.html')
            cc = Context({'name': Bname, 'email': Bemail, 'contain': Bdescripe, 'url': Burl})
            text_content = text.render(cc)
            html_content = html.render(cc)
            #
            # #  ���ڿ�ʼ�����ʼ�ʵ��
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))
    else:
        form = BugForm()
    return render_to_response('bug/bugpost.html', {'form': form}, context_instance=RequestContext(request))


def BugSuccess(request):
    """�ύbugת��ҳ��"""
    return render_to_response('bug/bugsuccess.html', context_instance=RequestContext(request))