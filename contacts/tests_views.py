from django.test import TestCase
from .forms import contactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

class ContactsTestViews(TestCase):
    def test_get_contacts_page(self):
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts.html")
    
    def test_thanks_page_can_be_rendered(self):
        response = self.client.get("/contacts/thanks/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "thanks.html")
    
    def test_fields_complete_contacts_form_is_valid(self):
        contact_form = contactForm({
            'full_name' : 'John Doe',
            'subject' : 'Example Subject',
            'from_email' : '123@example.com',
            'your_message' : 'Message here'
        })
        self.assertTrue(contact_form.is_valid())
        
        
    def test_field_email_incorrect_contacts_form_is_not_valid(self):
        contact_form = contactForm({
            'full_name' : 'John Doe',
            'subject' : 'Example Subject',
            'from_email' : 'example.com',
            'your_message' : 'Message here'
        })
        self.assertFalse(contact_form.is_valid())    
        self.assertTrue(HttpResponse('Make sure all fields are entered and valid.'))
        
    def test_able_to_send_email(self):
        contact_form = contactForm({
            'full_name' : 'John Doe',
            'subject' : 'Example Subject',
            'from_email' : '123@example.com',
            'your_message' : 'Message here'
        })
        self.assertTrue(contact_form.is_valid())
        response=self.client.post('/contacts/')
        self.assertEqual(response.status_code, 200)
        response=self.client.get('/contacts/thanks/')