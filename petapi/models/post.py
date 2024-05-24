from django.db import models
from .pet import Pet
from .petUser import PetUser
from django.contrib.auth.models import User

class Post(models.Model):
    description = models.CharField(max_length=200)
    sitStartDate = models.DateField()
    sitEndDate = models.DateField()
    publication_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField()
   
    pet_user = models.ForeignKey(PetUser, on_delete=models.CASCADE, related_name="posts")
    
    pets = models.ManyToManyField("Pet", through="PostPet", related_name="postpets")

    comments = models.ManyToManyField('Comment', related_name='postcomments', blank=True)
    likes = models.ManyToManyField(User, related_name='postlikes', blank=True)

 
  
