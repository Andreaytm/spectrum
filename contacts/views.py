# Django Contact Form taken and adapted from:https://wsvincent.com/django-contact-form/
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import contactForm
from .models import contact


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
            your_email = contact_form.cleaned_data['your_email']
            your_message = contact_form.cleaned_data['your_message']

            try:
                fullmessage = "Your Message: \n" + your_message + "\n" + "\n" 
                + "From: \n" + "\n" + full_name + " \n " + "<" + your_email + ">"
                send_mail(subject, fullmessage, your_email, [email_address])
                send_mail("Thank you for contacting Spectrum Ltd: " + subject, 
                "Thank you for contacting Spectrum Ltd." + "\n" + "\n" 
                + "We value your opinion and thoughts." + "\n" + "\n" 
                + "We will be in touch with you in the next 2 weeks." 
                + "\n" +"\n" 
                + "Please find below a copy of your email for your information." 
                + "\n" + "\n" + fullmessage, your_email, [your_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('thanks')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'contacts.html', {"contact_form": contact_form})


def thanks(request):
    return render(request, 'thanks.html')
