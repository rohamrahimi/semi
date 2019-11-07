from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2', )
