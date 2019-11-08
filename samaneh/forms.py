from django.contrib.auth.forms import *
from django import forms
from django.contrib.auth.models import User
from django.core import validators

from samaneh.models import Course
from . import models


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class Contact(forms.Form):
    title = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(validators=[validators.MinLengthValidator(10), validators.MaxLengthValidator(250)], required=True, widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MakeCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SettingForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name']