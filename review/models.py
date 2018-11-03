from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):
    
    """
    A single review
    """
    author = models.ForeignKey(User, blank=True, null=True)
    product = models.ForeignKey(Product, default=Product)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.title
