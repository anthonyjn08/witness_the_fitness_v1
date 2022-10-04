from django_summernote.widgets import SummernoteWidget
from .models import Post
from django import forms


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