from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    #path('<slugs>', views.blog_post, name='post'),
    path('search', views.search, name='search'),
]