from django.db import models
from users.models import CustomUser

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
