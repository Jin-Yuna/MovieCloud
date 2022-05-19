from django.db import models
from django.conf import settings
from movies.models import Movie

class Drop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='drops')
    movie = models.ForeignKey(Movie, on_delete=models.SET_DEFAULT, default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_vote = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_drops')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name='comments')
