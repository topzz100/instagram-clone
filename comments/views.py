from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Comment
from base.models import Post
import json
from django.contrib.humanize.templatetags.humanize import naturaltime

# Create your views here.

def commentHello(request):
    return HttpResponse("Hello world!")

def addComment(request): 
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body.decode('utf-8'))
            
            # Extract values from the JSON data
            comment = data.get('comment', '')
            postId = data.get('postId', '')
            post = Post.objects.get(id=postId)
            print(post)
            new_comment = Comment.objects.create(user=request.user, post=post, comment = comment)
            new_comment.save

            comment_data = {
                'id': new_comment.id,
                'comment': new_comment.comment,
                'username': new_comment.user.username,
                'profile_img': new_comment.user.profile.profile_img.url,
                # 'username': new_comment.user.username,
                # 'post': new_comment.post.id,
                # 'comment': new_comment.comment,
                # 'created_at': new_comment.created_at,
                'created_at': naturaltime(new_comment.created_at)
                # Add other fields as needed
            }
            
            # Perform necessary actions with the comment and postId
            # (e.g., save the comment to the database associated with the postId)
            
            # Return a JsonResponse with a success status and any additional data
            return JsonResponse({ "status": True, "comment": comment_data, "postId": postId })
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            return JsonResponse({"status": False, "error": "Invalid JSON data"})
    else:
        # Return an error response for non-POST requests
        return JsonResponse({"status": False, "error": "Invalid request method"})
    
