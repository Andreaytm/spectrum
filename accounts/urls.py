from django.conf.urls import url, include 
from .views import logout, login, registration, user_profile, edit_address
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password_reset/', include(url_reset)),
    url(r'^(?P<user_id>\d+)/edit_address/$', edit_address, name="edit_address")
]
