from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Address
from .forms import UserLoginForm, UserRegistrationForm, AddressForm
from checkout.models import OrderLineItem, Order
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))

def login(request):
    """Return a Login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method ==  "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user=auth.authenticate(username=request.POST['username'], 
            password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))

            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else: 
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse ('index'))
        
    if request.method =="POST":
        registration_form = UserRegistrationForm(request.POST)
        address_form = AddressForm(request.POST, request.FILES)

    
        if registration_form.is_valid()and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()
            
            user=auth.authenticate(username=request.POST['username'],
            password=request.POST['password1'])
        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:  
                messages.error(request, "Unable to register your account at this time")
    else:        
        registration_form = UserRegistrationForm()
        address_form = AddressForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form, 'address_form': address_form})

def user_profile(request):
    """ The user's profile page"""
    user= request.user
    address = Address.objects.filter(user=user)
    orderlineitem = OrderLineItem.objects.all()
    orders = Order.objects.all()
    return render(request, 'profile.html', {'address': address}) 

def edit_address(request, user_id=None):
    user = get_object_or_404(User, pk=user_id)
    address = get_object_or_404(Address, user=user) if user else None

    if request.method == "POST":
        addressform = AddressForm(request.POST, request.FILES, instance=address)
        if addressform.is_valid():
            address = addressform.save(commit=False)
            address.user = request.user
            deliveryaddress= address.save()
            return redirect(reverse(user_profile))
    else:
        addressform = AddressForm(instance=address)
    return render(request, 'address.html', {'addressform': addressform})