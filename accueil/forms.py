from django import forms
from .models import *


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryPhotos
        fields = ['title', 'images', 'parcours']