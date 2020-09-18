from django import forms

class ContactForm(forms.Form):
    F_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    L_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    subject = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)

class ApplicationForm(forms.Form):
    F_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    M_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    L_name = forms.CharField(max_length = 30, required=True, help_text='optional')
    email = forms.EmailField(max_length=100, required=True, help_text='required')
    phone_num = forms.IntegerField(required=True)
    course = forms.CharField(max_length=50, help_text='optional')
    message = forms.CharField(widget=forms.Textarea, required=True)