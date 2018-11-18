#Django Contact Form Adapted from:https://wsvincent.com/django-contact-form/
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import contactForm
from .models import contact

# Create your views here.
email_address = settings.EMAIL_HOST_USER

def contacts(request):
    """Allow user to send email to shop"""
    if request.method == "GET":
        contact_form = contactForm()
    else:
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            your_message = contact_form.cleaned_data['your_message']
            contacts = contact.objects.all()
            args= {'contacts': contacts}
            try:
                fullmessage = your_message + " " + full_name + " " + "<" + from_email + ">"
                send_mail(subject, fullmessage, from_email, [email_address])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('thanks')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'contacts.html', {"contact_form": contact_form})

def thanks(request):
    return render(request, 'thanks.html')
    