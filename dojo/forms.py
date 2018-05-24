from django import forms
from . models import GameUser, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
            # 'latlng': 
        }


    ''' 
    def save(self, commit=True):
        post = self.instance(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    '''


class GameUserForm(forms.ModelForm):
    model = GameUser
    fields = ['gameserver', 'username']


    def clean_username(self):
        return self.cleaned_data.get('username','').strip()
        