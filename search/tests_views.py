from django.test import TestCase
from products.models import Product

class SearchTestViews(TestCase):
    def test_do_search_template(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products.html")