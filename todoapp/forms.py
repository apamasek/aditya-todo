from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=100)

    class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status']
        