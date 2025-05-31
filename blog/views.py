from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Category, Tag, Article, Comment, Like
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer, CommentSerializer, LikeSerializer
from django.shortcuts import render
from blog.models import Article 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
# blog/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    return HttpResponse("Страница регистрации")

def home(request):
    return JsonResponse({"message": "Welcome to the Habr Clone API"})


@login_required
def profile(request):
    return render(request, 'profile.html')



@login_required
@require_http_methods(["GET", "POST"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comment_set.all()

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            article.comment_set.create(author=request.user, text=text)
            return redirect('article_detail', pk=article.pk)

    return render(request, 'article_detail.html', {'article': article, 'comments': comments})





@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content, author=request.user)
        return redirect('/')
    return render(request, 'create_article.html')


@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('/')
    return render(request, 'edit_article.html', {'article': article})


@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    article.delete()
    return redirect('/')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer





class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
