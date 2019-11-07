from django.conf.urls import url
from django.urls import path

from samaneh.views import home_page, signup, login, contact, contacted

urlpatterns = [
    path('', home_page),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('contact/', contact),
    path('contacted/', contacted)
]