from django.contrib import admin
from django.contrib import admin
from .models import Category, Tag, Article, Comment, Like

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
