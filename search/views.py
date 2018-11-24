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
