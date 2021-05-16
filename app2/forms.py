from django import forms
from .models import Post2

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post2
        fields = ['post2_title', 'post2_writer', 'post2_body', 'image']

