from django import forms
from django.forms import fields, widgets
from .models import UserFeedback
# from django.forms import widgets

# class Feedback(forms.Form):
#     email=forms.EmailField()
#     feedback=forms.CharField()

class Feedback(forms.ModelForm):
    class Meta:
        model=UserFeedback
        fields=['name','email','feedback']
        labels={'email':'Enter Email','feedback':'Write feedback','name':'Enter name'}
        widgets={'feedback':forms.Textarea(attrs={'cols': 100, 'rows': 5}),'email':forms.TextInput(attrs={'size':50})}
    
    