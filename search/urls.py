from django.conf.urls import url
from .views import (
    do_search, filter_product_name, sort_product_a_z, sort_product_z_a,
    sort_asc_cost, sort_desc_cost, filter_product_a2, filter_product_a3,
    filter_product_a4, filter_product_by_red, filter_product_by_orange,
    filter_product_by_yellow, filter_product_by_green, filter_product_by_blue,
    filter_product_by_purple, filter_product_by_black, filter_product_by_white,
    filter_product_by_pink)


urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^reviews/$', filter_product_name, name='filter'),
    url(r'^sort-a-z/$', sort_product_a_z, name='sort-a-z'),
    url(r'^sort-z-a/$', sort_product_z_a, name='sort-z-a'),
    url(r'^sort-asc-cost/$', sort_asc_cost, name='sort-asc-cost'),
    url(r'^sort-desc-cost/$', sort_desc_cost, name='sort-desc-cost'),
    url(r'^filter_product_a4/$', filter_product_a4, name='filter_product_a4'),
    url(r'^filter_product_a3/$', filter_product_a3, name='filter_product_a3'),
    url(r'^filter_product_a2/$', filter_product_a2, name='filter_product_a2'),
    url(r'filter_product_by_red/$', filter_product_by_red,
        name='filter_product_by_red'),
    url(r'filter_product_by_orange/$', filter_product_by_orange,
        name='filter_product_by_orange'),
    url(r'filter_product_by_yellow/$', filter_product_by_yellow,
        name='filter_product_by_yellow'),
    url(r'filter_product_by_green/$', filter_product_by_green,
        name='filter_product_by_green'),
    url(r'filter_product_by_blue/$', filter_product_by_blue,
        name='filter_product_by_blue'),
    url(r'filter_product_by_purple/$', filter_product_by_purple,
        name='filter_product_by_purple'),
    url(r'filter_product_by_white/$', filter_product_by_white,
        name='filter_product_by_white'),
    url(r'filter_product_by_black/$', filter_product_by_black,
        name='filter_product_by_black'),
    url(r'filter_product_by_pink/$', filter_product_by_pink,
        name='filter_product_by_pink'),
]
