from django.conf.urls import url, include
from .views import index, delivery, about

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^delivery/$', delivery, name='delivery'),
    url(r'^about/$', about, name='about'),
]