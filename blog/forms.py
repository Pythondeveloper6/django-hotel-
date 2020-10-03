from django import forms
from .models import Post , Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        # fields = ['title','content']
        exclude = ['created_at',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]