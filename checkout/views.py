from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
from accounts.models import Address
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    user = request.user
    address = Address.objects.filter(user=user)
    if request.method =="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
          
            cart = request.session.get('cart', {})
            total = 0
            delivery_cost = 4
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price + quantity * delivery_cost
                order_line_item = OrderLineItem(
                    order = order,
                    product = product, 
                    quantity = quantity,
                    user = user,
                    date = timezone.now()
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
                
            if customer.paid:
                messages.success(request, "You have successfully paid!")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card.")
    else:
        user = request.user
        address = Address.objects.filter(user=user)
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'address': address, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
