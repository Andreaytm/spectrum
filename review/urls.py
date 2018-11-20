from django.conf.urls import url
from .views import get_review, review_detail, create_or_edit_review, delete_review

urlpatterns = [
    url(r'^$', get_review, name='get_review'),   
    url(r'^(?P<pk_review>\d+)/$', review_detail, name='review_detail'),
    url(r'^new/$', create_or_edit_review, name='new_review'),
    url(r'^(?P<pk_review>\d+)/edit/$', create_or_edit_review, name='edit_review'),
    url(r'^(?P<pk_review>\d+)/delete/$', delete_review, name='delete_review')
    ]