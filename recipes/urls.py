from turtle import home
from django.contrib import admin
from django.http import HttpRequest
from django.urls import path,include
from .views import about,contact,home

#Domain.com/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about', about),
    path('contact', contact),
]