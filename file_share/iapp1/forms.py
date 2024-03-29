from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())#input in astricks form
    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('description', 'profile_pic')