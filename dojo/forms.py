from django import forms
from . models import Post


def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('Input more than 3 letters')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post