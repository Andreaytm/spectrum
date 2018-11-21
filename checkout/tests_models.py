from django.test import TestCase
from .models import Order
from django.utils import timezone

class CheckoutTestModels(TestCase):
    
    def test_str_checkout_order(self):
        test_order_str= Order(id='1', date='timezone.now()', full_name= 'Jane Doe')
        self.assertEqual(str(test_order_str), ('1-timezone.now()-Jane Doe'))
