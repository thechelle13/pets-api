from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=155)
    type = models.CharField(max_length=155)