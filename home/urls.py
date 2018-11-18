from django.conf.urls import url, include
from .views import index
from review.views import review_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk_review>\d+)/$', review_detail, name='review_detail'),
]