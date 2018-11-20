from django.test import TestCase
from .models import Address

class TestAddresssModel(TestCase):
    def test_str_address(self):
        test_address1= Address(address1 = '123 Lane')
        self.assertEqual(str(test_address1), '123 Lane')