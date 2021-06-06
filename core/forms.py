from django import forms
from django.forms import fields, widgets
from .models import UserFeedback

class Feedback(forms.ModelForm):
    class Meta:
        model=UserFeedback
        fields=['name','email','feedback']
        labels={'email':'Enter Email','feedback':'Write feedback','name':'Enter name'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'feedback':forms.Textarea(attrs={'class':'form-control'})}
    
