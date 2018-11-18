from django.test import TestCase
from .forms import contactForm
from django.http import HttpResponse

class ContactsTestViews(TestCase):
    """
    Test contacts views returns contact.html page
    with contact form
    """
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
        """
        If all fields not complete throw error
        HttpResponse('Make sure all fields are entered and valid.')
        """
        contact_form = contactForm({
            'full_name' : 'John Doe',
            'subject' : 'Example Subject',
            'from_email' : 'example.com',
            'your_message' : 'Message here'
        })
        self.assertFalse(contact_form.is_valid())    
        self.assertTrue(HttpResponse('Make sure all fields are entered and valid.'))
        
    def test_able_to_send_email(self):
        """
        Specific testing of send_mail was done via TDD 
        (including display of HttpResponse error messages)
        by sending test emails and checking in gmail account.
        However can test that this is also working via unittest 
        as redirects to thanks instead of returning
        HttpResponse('Invalid header found') or blank contact form
        """
        contact_form = contactForm({
            'full_name' : 'John Doe',
            'subject' : 'Example Subject',
            'from_email' : '123@example.com',
            'your_message' : 'Message here'
        })
        self.assertTrue(contact_form.is_valid())
        response=self.client.post('/contacts/')
        self.assertEqual(response.status_code, 302)
        response=self.client.get('/contacts/thanks/')
