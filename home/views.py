from django.shortcuts import render
from products.models import Product
from review.models import Review

def index(request):
    """ A view that displays the index page """
    product = Product.objects.all()[:6]
    review = Review.objects.all()[:3]
    args= {'product':product, 'review': review}
    return render(request, "index.html", args)

def about(request):
    return render(request, "about.html")

def delivery(request):
    return render(request, "delivery.html")