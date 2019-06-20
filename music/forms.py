from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','email','password']
