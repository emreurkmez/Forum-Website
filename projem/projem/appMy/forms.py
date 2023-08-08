from django import forms
from .models import Content
from appMy.models import Profile

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'content', 'image']

class FileUploadForm(forms.Form):
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'required': False}),
        }