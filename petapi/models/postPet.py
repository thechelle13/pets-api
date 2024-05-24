from django.db import models

class PostPet(models.Model):
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name="pet_posts")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_pets_set")
