from django.urls import path

from samaneh.views import home_page

urlpatterns = [
    path('', home_page)
]