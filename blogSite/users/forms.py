from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
