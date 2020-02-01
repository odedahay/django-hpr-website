from django.contrib import admin
from .models import Category, Post

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'author', 'category', 'created')
    list_display_links = ('id', 'title')
    list_filter = ('created', )
    list_editable = ('is_published',)
    search_fields = ('title', 'category')

admin.site.register(Post, BlogAdmin)
admin.site.register(Category)

