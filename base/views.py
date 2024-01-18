from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Post, LikePost, Follow, Tag
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required
from uuid import UUID
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.humanize.templatetags.humanize import naturaltime

# Create your views here.
def loginUser(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.error(request, 'Username OR password does not exit')
    return render(request, 'base/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if  password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, 'username is taken')
                else:
                    user = form.save()
                    Profile.objects.create(user=user, full_name=form.cleaned_data['full_name'])
                    login(request, user)
                    return redirect('/')
            else:
                messages.error(request, 'Passwords do not match')
        else:
            username_errors = form.errors.get('username', [])
            if username_errors:
                messages.error(request, f'Username: {username_errors[0]}')
            # messages.error(request, 'Error signing up. Please check the form')



    # if request.method == 'POST':
        # form = SignUpForm(request.POST)
        # print(request.POST)
        # print(form.is_valid())

        # if form.is_valid():
        #     user = form.save()
        #     Profile.objects.create(user=user, full_name=form.cleaned_data['full_name'])
        #     login(request, user)
        #     return redirect('/')
        
        # else:
        #     form = SignUpForm()
        #     if request.POST['password1'] != request.POST['password2']:
        #         messages.error(request, 'Passwords do not match')
        #     else: 
        #         messages.error(request, 'Error signing up. Please check the form')

   
    return render(request, 'base/signup.html', {'form': form})

@login_required(login_url='login')
def profile(request): 
    user_profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user = request.user)
    all_followers = Follow.objects.filter(followed=request.user.username)
    followings = Follow.objects.filter(user=request.user.username)

    followers =[]

    for follow in all_followers:
        followers.append(follow.followed)
    
    # if request.method == "POST":
    #     profile = user.profile 
    #     # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    #     # user_form = UpdateUserForm(request.POST, instance=request.user)

    #     # user_form = UpdateUserForm(request.POST, instance=user)
    #     profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
    #     print(profile_form.is_valid())

    #     # if profile_form.is_valid() and user_form.is_valid():
    #     if profile_form.is_valid():
    #         profile_form.save()
    #         # user_form.save()
    #         messages.success(request, 'Profile updated successfully!')
    #         return redirect('base/profile.html')
    #     else:
    #         messages.error(request, 'Error updating your profile. Please check the form')

    # else:
    #     # user_form = UpdateUserForm(instance=user)
    #     profile_form = Profile.objects.get(user=user.profile)

    # profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'base/profile.html', {'user_profile': user_profile, 'posts': posts, "followers": followers, "followings": followings})

def profile_user(request, pk):
    # user = User.objects.get(username=pk)
    user = get_object_or_404(User, username=pk)
    user_profile =  get_object_or_404(Profile, user=user)
    posts = Post.objects.filter(user = user_profile.user)
    all_followers = Follow.objects.filter(followed=pk)
    followings = Follow.objects.filter(user=pk)

    followers =[]

    for follow in all_followers:
        followers.append(follow.followed)

    # for follow in all_followings:
    #     followers.append(follow.user)

    print(followers)

    return render(request, 'base/profile.html', {'user_profile': user_profile, 'posts': posts, "followers": followers, "followings": followings})

@login_required(login_url='login')
def profile_update(request):
    user = request.user
    
    if request.method == "POST":
        profile = user.profile 
        # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # user_form = UpdateUserForm(request.POST, instance=request.user)

        # user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        print(profile_form.is_valid())

        # if profile_form.is_valid() and user_form.is_valid():
        if profile_form.is_valid():
            profile_form.save()
            # user_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your profile. Please check the form')

    else:
        # user_form = UpdateUserForm(instance=user)
        # profile_form = ProfileForm(instance=user.profile)
        profile_form = Profile.objects.get(user=request.user)
        print(profile_form.profile_img.url)
        
    return render(request, 'base/update-profile.html', {'profile_form': profile_form})

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

# @login_required(login_url='login')
def followUSer(request):
    if request.user.is_authenticated:
        # following = request.GET.get("following")
        # follow = Follow.objects.all()
        username = request.user.username
        followed = request.GET.get('followed_user')
        follow = Follow.objects.filter(user=username, followed=followed).first()

        if follow is None:
            addFollow = Follow.objects.create(user=username, followed=followed)
            addFollow.save()
            following=True

        else:
            follow.delete()
            following = False

        all_followers = Follow.objects.filter(followed=followed)
        
        new_followers = []
        for follow in all_followers:
            new_followers.append(follow.user)

        print(new_followers)
        return JsonResponse({"followed": followed, "following": following, "followers_count": new_followers, 'login': True})
    else:
         return JsonResponse({'login': False})

# def addComment(request): 
#     if request.method == 'POST':
#         try:
#             # Parse the incoming JSON data
#             data = json.loads(request.body.decode('utf-8'))
            
#             # Extract values from the JSON data
#             comment = data.get('comment', '')
#             postId = data.get('postId', '')
#             post = Post.objects.get(id=postId)
#             print(post)
#             new_comment = Comment.objects.create(user=request.user, post=post, comment = comment)
#             new_comment.save

#             comment_data = {
#                 'id': new_comment.id,
#                 'comment': new_comment.comment,
#                 'username': new_comment.user.username,
#                 'profile_img': new_comment.user.profile.profile_img.url,
#                 # 'username': new_comment.user.username,
#                 # 'post': new_comment.post.id,
#                 # 'comment': new_comment.comment,
#                 # 'created_at': new_comment.created_at,
#                 'created_at': naturaltime(new_comment.created_at)
#                 # Add other fields as needed
#             }
            
#             # Perform necessary actions with the comment and postId
#             # (e.g., save the comment to the database associated with the postId)
            
#             # Return a JsonResponse with a success status and any additional data
#             return JsonResponse({ "status": True, "comment": comment_data, "postId": postId })
#         except json.JSONDecodeError as e:
#             # Handle JSON decoding error
#             return JsonResponse({"status": False, "error": "Invalid JSON data"})
#     else:
#         # Return an error response for non-POST requests
#         return JsonResponse({"status": False, "error": "Invalid request method"})
    


def homepage(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    liked_posts =  LikePost.objects.filter(username = request.user.username)
    liked_posts_id = [UUID(post.post_id) for post in liked_posts]
    #  liked_posts_id = [f"UUID('{post.post_id}')" for post in liked_posts]
    # print (liked_posts_id)
    # if '8adeba1c-c5f9-4db5-b9cc-427cb58ee2e8' in liked_posts_id:
    #     print("true")
    # print(liked_posts_id)
    # posts_ids = []
    # for post in posts:
    #     posts_ids.append(post.id)

    # print(posts_ids)

    # posts_id = [post.id for post in posts]
    # print(posts_id)
    # for post in posts:
    #     if post.id in liked_posts_id:
    #         print(post.id)
    return render(request, 'base/home.html', {"profiles": profiles, "posts": posts, 'liked_posts': liked_posts_id})
