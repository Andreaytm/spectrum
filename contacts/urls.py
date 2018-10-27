from django.conf.urls import url
from contacts.views import contacts, thanks

urlpatterns = [
    url(r'^$', contacts, name='contacts'),
    url(r'^thanks/$', thanks, name='thanks'),
]