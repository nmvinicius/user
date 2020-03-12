from django import forms
from .models import User


class UserFormRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'avatar']


class UserFormLogin(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']
