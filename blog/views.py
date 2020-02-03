from django.shortcuts import render
from .models import Post, Category

def post_list(request):
    post_list = Post.objects.all()
    categories = Category.objects.all()    

    context = {
        'post_list': post_list,
        'categories': categories
    }
    return render(request, 'blog/post.html', context)

def post_by_category(request, category):
    categories = Category.objects.all() 
    post_by_category =  Post.objects.filter(category__category_name=category)

    context = {
        'post_list': post_by_category,
        'categories': categories
    }
    return render(request, 'blog/post.html', context)

def post_details(request, slug):
    post_details = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    latest_posts = Post.objects.order_by('-created').filter(is_published=True)[:3]   
   
    context = {
        'post_details': post_details,
        'categories': categories,
        'latest_posts':latest_posts
    }
    return render(request, 'blog/post-details.html', context)

def search(request):
    return render(request, 'blog/search.html')
