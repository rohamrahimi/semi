from django.conf.urls import url
from django.urls import path

from samaneh.views import *

urlpatterns = [
    path('', home_page),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('contact/', contact),
    path('contacted/', contacted, name='contacted'),
    path('logout/', logout),
    path('profile/', profile),
    path('panel/', go_panel),
    path('makecourse/', make_course),
    path('setting/', setting),
    path('courses/', go_courses)
]