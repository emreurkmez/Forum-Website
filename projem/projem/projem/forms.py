from django import forms
from appMy.models import Profile

class UserRegistrationForm(forms.Form):
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    profile_photo=forms.ImageField(required=False)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    agree_terms = forms.BooleanField()
    
