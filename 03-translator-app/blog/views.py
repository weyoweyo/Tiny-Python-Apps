from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post
from django.views import generic

class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


# post_list
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'