from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=64)
    data_published = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment from {self.author}'

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
