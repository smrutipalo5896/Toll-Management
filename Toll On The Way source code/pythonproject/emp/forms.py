from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        password=forms.CharField(widget = forms.PasswordInput)
        model=User
        fields=['username','email','password']