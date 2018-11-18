from django.db import models

# Create your models here.
class contact(models.Model):
    full_name = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    from_email = models.EmailField(max_length=80, blank=True)
    your_message = models.TextField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.full_name