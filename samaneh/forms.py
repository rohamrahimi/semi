from django.contrib.auth.forms import UserCreationForm
from django import forms

from . import models


class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100)

    class Meta:
        model = models.User
        fields = '__all__'
