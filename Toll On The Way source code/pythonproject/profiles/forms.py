from django import forms
from profiles.models import Post


class HomeForm(forms.ModelForm):
    first=forms.CharField(required=True)
    last=forms.CharField(required=True)
    vehicleno=forms.CharField(required=True)
    vehicletype=forms.CharField(required=True)
    journey_type=forms.CharField(required=True)
    
    class Meta:
        model=Post
        fields=('first','last','vehicleno','vehicletype','journey_type')
   