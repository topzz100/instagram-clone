from django.urls import path
from django.contrib.auth import views

from .views import homepage, loginUser, signup, profile, profile_user, profile_update, logoutUser, followUSer, explore

urlpatterns = [
    path('', homepage, name='homePage'),
    path('login/', loginUser, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile, name='profile' ),
    # path('upload/', uploadPost, name='upload_post'),
    # path('like/', likePost, name='like_post'),
    # path('like-post/', postLike, name='post_like'),
    path('follow-user/', followUSer, name='follow_user'),
    path('explore/', explore, name='explore'),
    path('<str:pk>/', profile_user, name='user_profile'),
    path('profile/update-profile/', profile_update, name='profile_modal'),

]
    # path('comment/', addComment, name='add_comment'),