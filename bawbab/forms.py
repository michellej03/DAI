# forms.py
from django import forms

class VerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'pattern': '\d{6}'}))

# You can create similar form classes for other steps
