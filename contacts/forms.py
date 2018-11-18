from django import forms
from .models import contact

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('full_name', 'subject', 'from_email', 'your_message')