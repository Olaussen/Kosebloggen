from django.shortcuts import render
from django.views import generic
from .models import Post
import random

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_list'] = set(random.choices(Post.objects.exclude(slug = Post.slug), k=3))
        return context

class AboutView(generic.TemplateView):
    template_name = 'blog/about.html'

class ContactView(generic.TemplateView):
    template_name = 'blog/contact.html'


