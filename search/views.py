from django.shortcuts import render
from products.models import Product
from review.models import Review


def do_search(request):
    products = Product.objects.filter(description__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})


def filter_product_name(request):
    products = Product.objects.all()
    review = Review.objects.filter(product__name__icontains=request.GET['z'])
    return render(request, "reviewposts.html", {
        "review": review, "products": products})


def sort_product_a_z(request):
    products = Product.objects.all().order_by('name')
    return render(request, "products.html", {"products": products})


def sort_product_z_a(request):
    products = Product.objects.all().order_by('-name')
    return render(request, "products.html", {"products": products})


def sort_asc_cost(request):
    products = Product.objects.all().order_by('price')
    return render(request, "products.html", {"products": products})


def sort_desc_cost(request):
    products = Product.objects.all().order_by('-price')
    return render(request, "products.html", {"products": products})


def filter_product_a4(request):
    products = Product.objects.filter(size='A4')
    return render(request, "products.html", {"products": products})


def filter_product_a3(request):
    products = Product.objects.filter(size='A3')
    return render(request, "products.html", {"products": products})


def filter_product_a2(request):
    products = Product.objects.filter(size='A2')
    return render(request, "products.html", {"products": products})


def filter_product_by_red(request):
    products = Product.objects.filter(tags__icontains='red')
    return render(request, "products.html", {"products": products})


def filter_product_by_orange(request):
    products = Product.objects.filter(tags__icontains='orange')
    return render(request, "products.html", {"products": products})


def filter_product_by_yellow(request):
    products = Product.objects.filter(tags__icontains='yellow')
    return render(request, "products.html", {"products": products})


def filter_product_by_green(request):
    products = Product.objects.filter(tags__icontains='green')
    return render(request, "products.html", {"products": products})


def filter_product_by_blue(request):
    products = Product.objects.filter(tags__icontains='blue')
    return render(request, "products.html", {"products": products})


def filter_product_by_purple(request):
    products = Product.objects.filter(tags__icontains='purple')
    return render(request, "products.html", {"products": products})


def filter_product_by_white(request):
    products = Product.objects.filter(tags__icontains='white')
    return render(request, "products.html", {"products": products})


def filter_product_by_black(request):
    products = Product.objects.filter(tags__icontains='black')
    return render(request, "products.html", {"products": products})


def filter_product_by_pink(request):
    products = Product.objects.filter(tags__icontains='pink')
    return render(request, "products.html", {"products": products})
