from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()
        return super().save(*args, **kwargs)


