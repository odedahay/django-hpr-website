from django.shortcuts import render
from .models import Post, Category

def post_list(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post.html', context)

def post_details(request, slug):
    post_details = Post.objects.get(slug=slug)

    context = {
        'post_details': post_details
    }
    return render(request, 'blog/post-details.html', context)

def search(request):
    return render(request, 'blog/search.html')
