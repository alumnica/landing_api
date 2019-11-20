#django
from django.urls import path
from django.conf.urls import url

from .views import ContactAPI, SuscriberAPI

urlpatterns = [
    url(r'^contact/$', ContactAPI.as_view()),
    url(r'^suscriber/$', SuscriberAPI.as_view()),
    ]