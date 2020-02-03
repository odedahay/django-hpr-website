from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey('Category', null=True,on_delete=models.SET_NULL)
    created = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug_name = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug_name and self.category_name:
            self.slug_name = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

