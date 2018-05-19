from django import forms

def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('Input more than 3 letters')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
