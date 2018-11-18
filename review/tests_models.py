from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from products.models import Product

class ReviewTestModel(TestCase):
    
    def test_can_create_a_review_if_logged_in(self):
        user=User.objects.create_user(
            username= 'user1',
            email= 'example@abc.com',
            password= 'password123')
        self.client.login(username ='user1',
            password='password123')
            
        product1= Product(name='name', description='content', price='5.00', image='product.image')
        product1.save()
        review = Review(title= 'Create a Test', content='name', product= product1, rating='five_stars')
        review.save()
        
        self.assertEqual(review.title, 'Create a Test')
        self.assertTrue(review.title)

    def test_review_as_a_string(self):
        """
        Test review models returns information as entered
        """
        example_title = Review(title='Test')
        self.assertEqual(str(example_title), 'Test')