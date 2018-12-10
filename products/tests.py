from django.test import TestCase
from .models import Product


class ProductTestModels(TestCase):
    def test_model_returns_information_entered(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


class ProductTestViews(TestCase):
    def setUp(self):
        self.products = Product.objects.filter()

    def test_get_products_page(self):
        response = self.client.get("/products/", self.products)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")
