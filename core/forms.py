from django import forms
from django.forms import widgets

class Feedback(forms.Form):
    email=forms.EmailField()
    feedback=forms.CharField()
