from django.test import TestCase
from django.contrib.auth.models import User


class TestRegistrationView(TestCase):
    def test_render_registration_form(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')


class TestLoginView(TestCase):
    def test_get_login_form(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")


class TestProfileView(TestCase):
    def test_render_profile(self):
        user1 = User.objects.create_user(
            username='user1',
            email='example@abc.com',
            password='password123')
        self.client.login(username='user1', password='password123')

        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestLogoutView(TestCase):
    def test_render_logout_form(self):
        user1 = User.objects.create_user(
            username='user1',
            email='example@abc.com',
            password='password123')
        self.client.login(username='user1', password='password123')

        response = self.client.post("/accounts/logout/")
        self.failureException('You have successfully been logged out!')

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
