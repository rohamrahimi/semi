from django.conf.urls import url
from django.urls import path

from samaneh.views import home_page, signup, login

urlpatterns = [
    path('', home_page),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login')
]