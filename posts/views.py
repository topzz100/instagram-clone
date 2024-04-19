from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, LikePost, Tag
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='login')
def uploadPost(request):
    # tags_list =- []
    if request.method == 'POST':
      
        user = request.user
        desc = request.POST['desc']
        postImg = request.FILES.get('post-upload')
        tags = request.POST['tags']
        # if tags is not None:
        #     all_tags = list(tags.split('#'))

        #     for tag in all_tags:
        #         t, created = Tag.objects.create(title=t, post=new_post)

        if postImg is not None:
            new_post = Post.objects.create(user=user, desc=desc, postImg=postImg)
            new_post.save()
            if tags is not None:
                all_tags = list(tags.split(' '))

                for tag in all_tags:
                    new_tag = tag.replace('#', '')
                    t = Tag.objects.create(title=new_tag, post=new_post)
                    t.save()
            return redirect('homePage')
    return redirect('/')

@login_required(login_url='login')
def likePost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    liked_post =  LikePost.objects.filter(post_id=post_id, username = username).first()
    print(liked_post)

    if liked_post is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes= post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        liked_post.delete()
        post.no_of_likes= post.no_of_likes-1
        post.save()
        return redirect('/')



def postLike(request):
    if request.user.is_authenticated:
        
    
        username = request.user.username
        # get the post id from the request data
        post_id = request.GET.get('post_id')
        # find the post object and update its likes
        post = Post.objects.get(id=post_id)
        liked_post =  LikePost.objects.filter(post_id=post_id, username = username).first()

        if liked_post is None:
            new_like = LikePost.objects.create(post_id=post_id, username=username)
            new_like.save()
            post.no_of_likes= post.no_of_likes+1
            post.save()
            # return redirect('/')
            liked = True
        else:
            liked_post.delete()
            post.no_of_likes= post.no_of_likes-1
            post.save()
            liked = False

        print(request.user.username,  "username")
        return JsonResponse({"liked": liked, "likes": post.no_of_likes, 'login': True})
    
    else:
        # return redirect('/')
        return JsonResponse({'login': False})
        
        # return redirect('/')
    # if post.likes.filter(id=request.user.id).exists():
    #     post.likes.remove(request.user)
    #     liked = False
    # else:
    #     post.likes.add(request.user)
    #     liked = True
    # return a JSON response with the liked status and the number of likes
    # print(request.user.username,  "username")
    # return JsonResponse({"liked": liked, "likes": post.no_of_likes})
