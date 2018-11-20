from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    cart= request.session.get('cart', {})
    
    cart_items= []
    total = 0
    product_count = 0
    delivery_cost = 4
    totaldeliverycost = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price + quantity * delivery_cost
        totaldeliverycost = quantity * delivery_cost
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        
    return { 'cart_items': cart_items, 'total' : total, 'totaldeliverycost': totaldeliverycost, 'product_count': product_count }
    