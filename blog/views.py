from django.shortcuts import render

def index(request):
    return render(request, 'blogs/blog.html')

def blog_post(request):
    return render(request, 'blogs/blog-post.html')

def search(request):
    return render(request, 'blogs/search.html')
