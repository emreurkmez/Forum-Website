from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Lütfen geçerli bir email adresi girin.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

