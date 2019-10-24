from django.db import models
# conf
from django.conf import settings 


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles')

    # () X / 들여쓰기
    class Meta:
        ordering = ('-pk', )


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk', )
