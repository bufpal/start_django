from django import forms
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    ''' 
    def save(self, commit=True):
        post = self.instance(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
    '''