from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from base.models import Post
import uuid

# Create your models here.
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE, null=True )
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment=models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment[:10]
    
    class Meta:
        ordering = ['-created_at']
