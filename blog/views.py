from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request=request, template_name='blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
