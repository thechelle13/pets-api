from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .pet import Pet
from .petUser import PetUser
from .comment import Comment
from django.contrib.auth.models import User  # Import the User model

class Post(models.Model):
    description = models.CharField(max_length=200)
    sitStartDate = models.DateField()
    sitEndDate = models.DateField()
    publication_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    pet_user = models.ForeignKey(PetUser, on_delete=models.CASCADE, related_name="posts")
    
    comments = models.ManyToManyField(Comment, related_name='post_comments', blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

@receiver(pre_delete, sender=Post)
def delete_related_comments_and_likes(sender, instance, **kwargs):
    instance.comments.clear()
    instance.likes.clear()
