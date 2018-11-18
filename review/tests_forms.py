from django.test import TestCase
from .forms import ReviewForm
from products.models import Product

class ReviewTestForm(TestCase):

    def test_throw_error_if_missing_review_content(self):
        reviewform = ReviewForm({'title': ''})
        self.assertFalse(reviewform.is_valid())
        self.assertEqual(reviewform.errors['title'], [u'This field is required.'])
