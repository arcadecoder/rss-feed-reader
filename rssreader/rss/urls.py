from django import urls
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='homepage')
]