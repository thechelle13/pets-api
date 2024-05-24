from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

 
