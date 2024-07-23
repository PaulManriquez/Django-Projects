from django import forms 

class FormContact(forms.Form):
    Name = forms.CharField(label='Name',required=True)
    Email = forms.CharField(label='Email',required=True)
    Content = forms.CharField(label='Content',widget=forms.Textarea)
