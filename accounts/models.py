from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=40, blank=False)
    address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    
    def __str__(self):
        return self.address1