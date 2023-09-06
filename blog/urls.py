from django.urls import path
from .views import PostListView
from . import views


urlpatterns = [
    # path(route='', view=views.home, name='blog-home'),
    path(route='', view=PostListView.as_view(), name='blog-home'),
    path(route='about/', view=views.about, name='blog-about'),
]
