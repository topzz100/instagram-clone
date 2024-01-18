from django.urls import path
from django.contrib.auth import views
from .views import addComment, commentHello

urlpatterns = [
    path('add/', addComment, name='add_comment'),
    path('hello/', commentHello, name='comment_hello'),
]