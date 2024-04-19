from django.urls import path
from django.contrib.auth import views
from .views import likePost, postLike, uploadPost

urlpatterns = [
     path('upload/', uploadPost, name='upload_post'),
    path('like/', likePost, name='like_post'),
    path('like-post/', postLike, name='post_like'),
]