# forms.py
from django import forms

class CheckoutForm(forms.Form):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    physical_address = forms.CharField(required=False)
