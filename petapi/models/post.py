from django.db import models
from .pet import Pet


class Post(models.Model):
    description = models.CharField(max_length=200)
    sitStartDate = models.DateField()
    sitEndDate = models.DateField()
    publication_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # city = models.CharField(max_length=155)
    pet_user = models.ForeignKey("PetUser", on_delete=models.CASCADE, related_name="posts")


