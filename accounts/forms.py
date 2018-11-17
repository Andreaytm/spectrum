from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Address

class UserLoginForm(forms.Form):
    """Form to be used to log users in"""
    username = forms.CharField(
    label="Username/ Email Address")
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
        
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)
    
    first_name= forms.CharField(
        label="First Name",
        )
        
    last_name= forms.CharField(
        label="Last Name",
        )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
            
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
            
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('full_name', 'address1', 'address2', 'town_or_city', 'county', 'postcode', 'country')