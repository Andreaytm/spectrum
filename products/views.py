from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'products.html', {"products": products})
