from django.shortcuts import render
from products.models import Product
from review.models import Review


def do_search(request):
    products = Product.objects.filter(description__icontains=request.GET['q'])
    return render(request, "products.html", {"products" : products})
    
def filter_product_name(request):
    products = Product.objects.all()
    review = Review.objects.filter(product__name__icontains=request.GET['z'])
    return render(request, "reviewposts.html", {"review" : review, "products" : products})

def sort_product_a_z(request):
    products = Product.objects.all().order_by('name')
    return render(request, "products.html", {"products" : products})

def sort_product_z_a(request):
    products = Product.objects.all().order_by('-name')
    return render(request, "products.html", {"products" : products})

def sort_asc_cost(request):
    products = Product.objects.all().order_by('price')
    return render(request, "products.html", {"products" : products})

def sort_desc_cost(request):
    products = Product.objects.all().order_by('-price')
    return render(request, "products.html", {"products" : products})
    
def filter_product_a4(request):
    products = Product.objects.filter(name__icontains='A4')
    return render(request, "products.html", {"products" : products})

def filter_product_a3(request):
    products = Product.objects.filter(name__icontains='A3')
    return render(request, "products.html", {"products" : products})

def filter_product_a2(request):
    products = Product.objects.filter(name__icontains='A2')
    return render(request, "products.html", {"products" : products})