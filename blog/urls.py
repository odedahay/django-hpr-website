from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('category=<slug:category>', views.post_by_category, name='post_by_category'),
    path('<slug:slug>', views.post_details, name='post_details'),
    path('search', views.search, name='search'),
]