from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'name']
