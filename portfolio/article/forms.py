from django import forms
from django.forms import ModelForm

from .models import *

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'addphoto', 'id': 'file1'}),
        }