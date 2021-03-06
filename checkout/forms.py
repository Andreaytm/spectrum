from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2037)]

    credit_card_number = forms.CharField(
        label='Credit/Debit card number',
        help_text="Please enter your 16-digit card number.", required=False)
    cvv = forms.CharField(
        label='Security code (CVV)',
        help_text="The CVV code can be found on the back of your card.",
        required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'address1', 'address2', 'town_or_city',
            'county', 'postcode',  'country')
