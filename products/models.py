from django.db import models

class Product(models.Model):
    
    A4= 'A4'
    A3= 'A3'
    A2= 'A2'
    
    SIZE_CHOICES = (
        (A4, 'A4'),
        (A3, 'A3'),
        (A2, 'A2'),)
        
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, default='A4')
    tags = models.CharField(max_length=254, default='')

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name