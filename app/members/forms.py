from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._user = None

    username = forms.CharField(
        widget= forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean(self):
        super().clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('invalid username or password')
        self._user = user

    @property
    def user(self):
        if self.errors:
            raise ValueError('form validation failed')
        return self._user


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username already exists')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('password does not match')
        return password2

    def save(self):
        if self.errors:
            raise ValueError('form validation failed')
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
        return user
