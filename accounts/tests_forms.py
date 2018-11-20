from django.test import TestCase
from .forms import UserRegistrationForm

class TestRegistrationForms(TestCase):
    def test_registration_form_passwords_do_not_match_form_is_not_valid(self):
        """
        Test that password1 and password2 must match to be able to register
        otherwise registration_form is not valid
        """
        registration_form = UserRegistrationForm({
            'first_name' :'John',
            'last_name' :'Doe',
            'username':'example',
            'email' : 'testuser@example.com',
            'password1' : 'Password01',
            'password2' : 'Password99'
        })
        self.assertFalse(registration_form.is_valid())
        
    def test_registration_form_all_fields_complete_form_is_valid(self):
        """
        Test if fill in all fields registration_form is valid
        """
        registration_form = UserRegistrationForm({
            'first_name' : 'John',
            'last_name' : 'Doe',
            'username': 'example',
            'email' : 'testuser@example.com',
            'password1' : 'Password01',
            'password2' : 'Password01'
        })
        self.assertTrue(registration_form.is_valid())
    