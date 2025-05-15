from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('', lambda request: JsonResponse({"message": "Welcome to the Habr Clone API"})),
]
