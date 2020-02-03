from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def index(request):
    latest_post = Post.objects.order_by('-created').filter(is_published=True)[:3]

    context = {
        'latest_post':latest_post
    }
    
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/service.html')
