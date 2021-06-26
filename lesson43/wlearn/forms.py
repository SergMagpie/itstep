from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.creator = kwargs['initial']['creator']
        super(AddPostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(AddPostForm, self).save(False)
        obj.creator = self.creator
        commit and obj.save()
        return obj

    class Meta:
        model = Words
        fields = ['word', 'translate', 'learned']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-input'}),
            'translate': forms.TextInput(attrs={'class': 'form-input'}),
            'learned': forms.CheckboxInput(attrs={'class': 'form-input'}),
        }
