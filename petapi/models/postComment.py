from django.db import models

class PostComment(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="post_comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_comments_set")
