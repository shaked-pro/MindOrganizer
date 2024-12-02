from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Thought
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content']
        exclude = ['author']

class UpdateThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content']
        exclude = ['author']