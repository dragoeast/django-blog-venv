from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
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

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
