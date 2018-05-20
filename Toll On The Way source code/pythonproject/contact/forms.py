from django import forms
class contactforms(forms.Form):
    name = forms.CharField(required=False,max_length=100,help_text='100 chars')                           
    email = forms.EmailField(required=True,max_length=200)
    comment = forms.CharField(required=True,widget=forms.Textarea)