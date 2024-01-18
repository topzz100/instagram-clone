from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    # full_name = forms.CharField(max_length=100, required=True)
    # email = forms.EmailField(max_length=255, required=True)
    full_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your first name.")

    class Meta:
        model = User
        fields = ['full_name', 'username',  'email', 'password1', 'password2']

# class UpdateUserForm(forms.ModelForm):
#     # full_name = forms.CharField(max_length=100, required=True)
#     # email = forms.EmailField(max_length=255, required=True)
#     full_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your first name.")
#     class Meta:
#         model = User
#         fields = ['username', 'full_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'gender', 'profile_img']
