from django import forms
from .models import Comment, Post
from start_django.widgets.naver_map_point_widget import NaverMapPointWidget


class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width': "100%", 'height': 500}))

    class Meta:
        model = Post
        fields = ['status', 'title', 'content', 'photo', 'lnglat', 'tag_set']
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={'width': 600, 'height': 400}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']