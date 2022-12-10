from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'featured_image',
            'excerpt',
            'content',
        ]

        widgets = {
                'content': SummernoteWidget(),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
