from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    totalproductcost = 0
    product = 0
    product_count = 0
    delivery_cost = 4
    totaldeliverycost = 0
    free_delivery = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        totalproductcost += quantity * product.price
        product_count += quantity
        total =  totalproductcost + totaldeliverycost
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    if totalproductcost >= 100:
        totaldeliverycost = 0
        free_delivery = 0
    else:
        totaldeliverycost = product_count * delivery_cost
        free_delivery = 100 - totalproductcost
    
    return {
        'cart_items': cart_items, 'total': total,
        'totaldeliverycost': totaldeliverycost, 'product': product,
        'totalproductcost': totalproductcost, 'free_delivery': free_delivery,
        'product_count': product_count}
