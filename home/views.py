from django.shortcuts import render
from products.models import Product
from review.models import Review
from django.utils import timezone
import random


def index(request):
    """ A view that displays the index page """
    foo = [
        'pink', 'orange', 'yellow', 'green', 'blue',
        'red', 'purple', 'white', 'black']
    option = random.choice(foo)
    product = Product.objects.filter(tags__icontains=option)[:3]
    review = Review.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:3]
    args = {'product': product, 'review': review}
    return render(request, "index.html", args)


def about(request):
    return render(request, "about.html")


def delivery(request):
    return render(request, "delivery.html")
