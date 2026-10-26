from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "status"]
        widgets = {
            "content": forms.Textarea(attrs={"rows":5})
        }
        labels = {
            "title": "заголовок",
            "content": "содержание",
            "category":"категория",
            "status" : "статус"
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')
        