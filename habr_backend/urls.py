from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import home
from blog.views import create_article 
from blog.views import edit_article
from blog.views import delete_article

from blog.views import profile
from blog.views import register


from blog.views import article_detail
from django.contrib.auth import views as auth_views
from blog import views


urlpatterns = [
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/create/', create_article, name='create_article'),
    path('articles/<int:pk>/edit/', edit_article, name='edit_article'),
    path('articles/<int:pk>/delete/', delete_article, name='delete_article'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', views.home),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]