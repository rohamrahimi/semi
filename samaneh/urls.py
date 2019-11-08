from django.conf.urls import url
from django.urls import path


from samaneh.views import home_page, signup, login, contact, contacted, logout, profile, go_panel

from samaneh.views import home_page, signup, login, contact, contacted, logout, profile, setting

urlpatterns = [
    path('', home_page),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('contact/', contact),
    path('contacted/', contacted),
    path('logout/', logout),
    path('profile/', profile),
    path('panel/', go_panel),
    path('setting/', setting)
]