from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

    # Adding LoginRequiredMixin to the CreateView class
    # that we inherit from to the first left side 
    # to enforce logged in to create a new post. 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
