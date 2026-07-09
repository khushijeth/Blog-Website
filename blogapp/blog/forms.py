from django import forms
from . models import Blog
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
   class Meta:
        model = Blog
        fields = [
            "title",
            "author",
            "image",
            "content",
        ]

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields=["username","email","password1","password2"]