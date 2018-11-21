from django.test import TestCase
from .models import Order
from .forms import OrderForm, MakePaymentForm

class TestCheckoutForm(TestCase):
    def test_checkout_form_not_valid_if_missing_fields(self):
        order_form=OrderForm({'full_name': 'John Doe'})
        self.assertFalse(order_form.is_valid())
    
    def test_checkout_form_is_valid_if_fields_complete(self):
        order_form=OrderForm({
            'full_name': 'John Doe',
            'address1': '123 Lane', 
            'address2': 'Hello Street', 
            'town_or_city': 'Orange City', 
            'county': 'NewCounty', 
            'postcode': 'PK1',  
            'country': 'UK'
        })
        self.assertTrue(order_form.is_valid())
        
class TestMakePaymentForm(TestCase):
    def test_MakePaymentForm_is_valid_if_fields_complete(self):
        payment_form=MakePaymentForm({
            'credit_card_number':'4242424242424242',
            'cvc':'123',
            'expiry_month':'12',
            'expiry_year':'2022',
            'stripe_id':'widget=forms.HiddenInput'
        })
        self.assertTrue(payment_form.is_valid())