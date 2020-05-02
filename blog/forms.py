from .models import Comment
from django import forms
from blog.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email','body')