from django import forms
from .widgets import CustomClearableFileInput
from .models import Sports


class SportForm(forms.ModelForm):
    """ Form to add new sports """

    class Meta:
        model = Sports
        fields = '__all__'

    sport_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
