from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views


urlpatterns = [
    path(route='', view=PostListView.as_view(), name='blog-home'),
    path(route='user/<str:username>', view=UserPostListView.as_view(), name='user-posts'),
    path(route='post/<int:pk>', view=PostDetailView.as_view(), name='post-detail'),
    path(route='post/new', view=PostCreateView.as_view(), name='post-create'),
    path(route='post/<int:pk>/update/', view=PostUpdateView.as_view(), name='post-update'),
    path(route='post/<int:pk>/delete/', view=PostDeleteView.as_view(), name='post-delete'),
    path(route='about/', view=views.about, name='blog-about'),
]
