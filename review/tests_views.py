from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .forms import ReviewForm 
from django.utils import timezone 


class ReviewTestViews(TestCase):

    def test_get_main_review_page(self):
        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviewposts.html")

    def test_cannot_create_review_if_form_not_valid(self):
        User.objects.create_user(
            username= 'user1',
            email= 'example@abc.com',
            password= 'password123')
        self.client.login(username ='user1',
            password='password123')
            
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        
    def test_add_review(self):
        User.objects.create_user(
            username= 'user1',
            email= 'example@abc.com',
            password= 'password123')
        self.client.login(username ='user1',
            password='password123')
            
        product1= Product.objects.create(
            name='product1', 
            description='content', 
            price='5.00', 
            image='image.jpg')

        response = self.client.get("/reviews/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviewform.html")
        
        review = Review.objects.create(
            title = 'Create a Test', 
            content='name', 
            product= product1, 
            rating="five_stars", 
            image="reviewimage.jpg")
            
        response=self.client.get("/reviews/{0}/".format(review.id))

    def test_get_specific_review_detail_page(self):
        product1= Product.objects.create(
            name='product1', 
            description='content', 
            price='5.00', 
            image='image.jpg')

        review = Review.objects.create(
            title = 'Create a Test', 
            content='name', 
            product= product1, 
            rating="five_stars", 
            image="reviewimage.jpg")
            
        response = self.client.get("/reviews/{0}/".format(review.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviewdetail.html")
