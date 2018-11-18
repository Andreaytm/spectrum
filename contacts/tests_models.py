from django.test import TestCase
from .models import contact

class ContactTestModels(TestCase):
    def test_str(self):
        test_contact_full_name= contact(full_name= 'Jane Doe')
        self.assertEqual(str(test_contact_full_name), 'Jane Doe')
