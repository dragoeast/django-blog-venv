from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.home, name='blog-home'),
    path(route='about/', view=views.about, name='blog-about'),
]
