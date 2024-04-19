from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import uuid

# User = get_user_model()

# class CustomUser(AbstractUser):
#     full_name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True, default='')
    bio = models.TextField(blank=True, null=True, default='')
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username  
    

# class Post(models.Model):
#     user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
#     id= models.UUIDField(primary_key=True, default=uuid.uuid4)
#     postImg = models.ImageField(upload_to='profile_images', default='demo-image-default') 
#     # caption = models.TextField(null=True, blank=True)
#     desc = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(default=datetime.now)
#     no_of_likes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user.username   

# class Tag(models.Model):
#     title = models.CharField(max_length=100)
#     post = models.ForeignKey(Post, related_name='tags', on_delete=models.CASCADE ) 

#     def __str__(self):
#         return self.title   
    
# class LikePost(models.Model):
#     post_id = models.CharField(max_length=500)
#     username = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username
    

class Follow(models.Model):
    followed = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

 
# class Comment(models.Model):
#     post=models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
#     user=models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE, null=True )
#     id= models.UUIDField(primary_key=True, default=uuid.uuid4)
#     comment=models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return self.comment[:10]
    
#     class Meta:
#         ordering = ['-created_at']
