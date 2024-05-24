from django.db import models

class PostLike(models.Model):
    like = models.ForeignKey("Like", on_delete=models.CASCADE, related_name="like_posts")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_likes_set")
