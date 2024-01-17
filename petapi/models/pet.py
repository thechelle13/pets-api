from django.db import models
from .type import Type 


class Pet(models.Model):
    name = models.CharField(max_length=155)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)