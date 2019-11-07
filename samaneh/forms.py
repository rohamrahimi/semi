from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from . import models


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'first_name', 'password1', 'password2']
