from django.test import TestCase
from .forms import contactForm

class TestContactForm(TestCase):
    
    def test_can_contact(self):
        contact_form = contactForm({'full_name': 'John Doe'})
        self.assertTrue(contact_form.is_valid())
