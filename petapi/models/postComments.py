from django.db import models
from .post import Post
from .comment import Comment

class PostComments(models.Model):
    # post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_comments")
    # comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="post_comments")
    
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments_relation")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="post_comments_relation")