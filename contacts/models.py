from django.db import models

# Create your models here.
class contact(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    your_email = models.EmailField(max_length=80, blank=False)
    your_message = models.TextField(max_length=1000, blank=False)
    
    def __str__(self):
        return self.full_name