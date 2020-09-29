from django import forms
from .models import Application

class ContactForm(forms.Form):
    First_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    Surname = forms.CharField(max_length = 30, required=True, help_text='optional')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    subject = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)

class ApplicationForm(forms.Form): 
    First_Name = forms.CharField(max_length = 30, required=True, help_text='optional')
    Middle_Name = forms.CharField(max_length = 30, required=True)
    Surname = forms.CharField(max_length = 30, required=True, help_text='optional')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    phone_num = forms.IntegerField(required=True )
    course = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)