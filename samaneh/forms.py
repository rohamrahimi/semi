from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core import validators

from . import models


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'first_name', 'password1', 'password2')


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class Contact(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(validators=[validators.MinLengthValidator(10), validators.MaxLengthValidator(250)], required=True, widget=forms.Textarea)
