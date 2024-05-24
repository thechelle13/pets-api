from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .post import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

    

