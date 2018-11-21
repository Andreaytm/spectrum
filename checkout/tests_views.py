from django.test import TestCase
from .forms import MakePaymentForm, OrderForm
from django.contrib.auth.models import User
from accounts.models import Address
from django.conf import settings
import stripe

class TestCheckoutViews(TestCase):
    def test_get_checkout_page(self):
        user=User.objects.create_user(
            username= 'user1',
            email= 'example@abc.com',
            password= 'password123')
        self.client.login(username ='user1',
            password='password123')
        stripe.api_key = settings.STRIPE_SECRET
        address = Address.objects.filter(user=user)
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        response = self.client.get("/checkout/", {'address': address, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
        self.assertTemplateUsed(response, "checkout.html")
