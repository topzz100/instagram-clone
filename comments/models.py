from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from posts.models import Post
import uuid

# Create your models here.
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True )
    comment=models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, )

    def __str__(self):
        return self.comment[:10]
    
    class Meta:
        ordering = ['-created_at']
