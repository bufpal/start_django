from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['status', 'title', 'content', 'image', 'lnglat', 'tag_set']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']