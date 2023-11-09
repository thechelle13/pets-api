from django.db import models


class Post(models.Model):
    description = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    sitStartDate = models.CharField(max_length=155)
    sitStartEnd = models.CharField(max_length=155)