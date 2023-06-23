from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username')
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
            'email':'Email',
            'username':'Username',
            'password1':'Password',
            'password2':'Password(ag)'
        }

