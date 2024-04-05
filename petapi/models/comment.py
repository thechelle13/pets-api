from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

