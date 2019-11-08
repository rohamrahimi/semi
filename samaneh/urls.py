from django.conf.urls import url
from django.urls import path

<<<<<<< Updated upstream
from samaneh.views import home_page, signup, login, contact, contacted, logout, profile, go_panel
=======
from samaneh.views import home_page, signup, login, contact, contacted, logout, profile, setting
>>>>>>> Stashed changes

urlpatterns = [
    path('', home_page),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('contact/', contact),
    path('contacted/', contacted),
    path('logout/', logout),
    path('profile/', profile),
<<<<<<< Updated upstream
    path('panel/', go_panel)
=======
    path('setting/', setting)
>>>>>>> Stashed changes
]