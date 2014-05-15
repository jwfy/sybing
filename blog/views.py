# -*- coding: utf-8 -*-

from blog.models import Blog
from django.views.generic import ListView, DetailView
# from blog.models import BlogComments
# from django.db.models.expressions import F
# from blog.forms import BlogCommentsForm
# from django.views.generic.edit import FormView


class BlogListViewByPage(ListView):
    """博客的具体列表"""
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
    paginate_by = 6


class BlogDetailViewById(DetailView):
    """ 博客的具体列表按照ID"""
    queryset = Blog.objects.all()
    context_object_name = 'article'
    template_name = 'blog/blog_detail.html'
    # form_class = BlogCommentsForm
    # success_url = 'succeed'

    def get_object(self):
        """获取当前页面显示的具体博客内容，浏览量加1"""
        object = super(BlogDetailViewById, self).get_object()
        object.count += 1
        object.save()
        return object

    # def get_context_data(self, **kwargs):
    #     """增加额外的相关数据，也就是form显示的数据和评论的相关数据"""
    #     self.object = self.get_object()
    #     contents = super(BlogDetailViewById, self).get_context_data(**kwargs)
    #     contents['form'] = BlogCommentsForm
    #     return contents
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     extra_context = {
    #         'article': self.object,
    #         'comments': BlogComments.objects.get_blog_comment(self.object)
    #     }
    #     return self.render_to_response(self.get_context_data(**extra_context))
    #
    # def post(self, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class BlogListViewByCategory(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(cat=self.kwargs['id'])


class BlogListViewByTag(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(tags=self.kwargs['id'])


class BlogListViewBySearch(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Blog.objects.filter(Q(caption__icontains=q) | Q(content__icontains=q)).distinct()
