from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.pk})

class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
