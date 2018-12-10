from django.test import TestCase
from products.models import Product
from review.models import Review


class TestViews(TestCase):
    def setUp(self):
        self.product = Product.objects.all()[:6]
        self.review = Review.objects.all()[:3]

    def test_get_home_page(self):
        response = self.client.get("/", self.product, self.review)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_get_about_page(self):
        response = self.client.get("/home/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_get_delivery_page(self):
        response = self.client.get("/home/delivery/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delivery.html")
