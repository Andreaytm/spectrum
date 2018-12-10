from django.test import TestCase
from django.contrib.auth.models import User


class TestCartViews(TestCase):
    def test_render_cart_page(self):
        User.objects.create_user(
            username='user1',
            email='example@abc.com',
            password='password123')
        self.client.login(username='user1', password='password123')
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
