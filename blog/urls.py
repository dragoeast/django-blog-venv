from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    path(route='', view=PostListView.as_view(), name='blog-home'),
    path(route='post/<int:pk>', view=PostDetailView.as_view(), name='post-detail'),
    path(route='about/', view=views.about, name='blog-about'),
]
