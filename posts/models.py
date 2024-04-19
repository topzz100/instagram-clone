from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import uuid

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    postImg = models.ImageField(upload_to='profile_images', default='demo-image-default') 
    # caption = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username   

class Tag(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Post, related_name='tags', on_delete=models.CASCADE ) 

    def __str__(self):
        return self.title   
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
