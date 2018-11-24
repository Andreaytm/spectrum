from django.conf.urls import url 
from .views import do_search, filter_product_name, sort_product_a_z, sort_product_z_a, sort_asc_cost, sort_desc_cost

urlpatterns =[
    url(r'^$', do_search, name='search'),
    url(r'^reviews/$', filter_product_name, name='filter'),
    url(r'^sort-a-z/$', sort_product_a_z, name='sort-a-z'),
    url(r'^sort-z-a/$', sort_product_z_a, name='sort-z-a'),
    url(r'^sort-asc-cost/$', sort_asc_cost, name='sort-asc-cost'),
    url(r'^sort-desc-cost/$', sort_desc_cost, name='sort-desc-cost'),
    ]