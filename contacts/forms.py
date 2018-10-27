from django import forms

class contactForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True)
    subject = forms.CharField(max_length=50, required=True)
    from_email = forms.EmailField(required=True)
    your_message = forms.CharField(widget=forms.Textarea, required=True)

