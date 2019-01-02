from django import forms

from .models import DomesticCarTalkBoard


class PostForm(forms.ModelForm):
    class Meta:
        model = DomesticCarTalkBoard
        fields = [
            'title',
            'content',
            'tags',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'cols':50,'row':1}),
            'content' : forms.Textarea(attrs={'cols':80, 'row':20}),
        }