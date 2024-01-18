from django.db import models
from .type import Type
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=155)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_user')
    image_url = models.URLField(max_length=200)
    #image_url = models.CharField(max_length=200)