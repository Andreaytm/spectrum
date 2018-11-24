from django.conf.urls import url 
from .views import do_search, filter_product_name

urlpatterns =[
    url(r'^$', do_search, name='search'),
    url(r'^reviews/$', filter_product_name, name='filter')
    ]