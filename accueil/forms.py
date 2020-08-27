from django import forms
from .models import *


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryPhotos
        fields = ['title', 'images', 'parcours']
        field_classes = {
            'parcours': UserModelChoiceField
        }
