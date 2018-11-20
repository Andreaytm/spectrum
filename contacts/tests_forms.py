from django.test import TestCase
from .forms import contactForm

class TestContactForm(TestCase):
    
    def test_can_contact_spectrum(self):
        contact_form = contactForm({
            'full_name': 'John Doe',
            'subject': 'Example Message', 
            'from_email': '1user@gmail.com', 
            'your_message': 'Hello there'
        })
        self.assertTrue(contact_form.is_valid())
    
    def test_form_is_not_valid_with_incomplete_fields(self):
        contact_form = contactForm({
            'full_name': 'John Doe',
            'subject': '', 
            'from_email': '1user@gmail.com', 
            'your_message': 'Hello there'
        })
        self.assertFalse(contact_form.is_valid())

    def test_form_is_not_valid_with_incorrect_email(self):
        contact_form = contactForm({
            'full_name': 'John Doe',
            'subject': 'Hello', 
            'from_email': '1user', 
            'your_message': 'Hello there'
        })
        self.assertFalse(contact_form.is_valid())