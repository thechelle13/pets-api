from django.db import models
from django.contrib.auth.models import User

class PetUser(models.Model):
    """Database model for tracking events"""

    bio = models.CharField(max_length=200)
    city = models.CharField(max_length=155)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pet_user")