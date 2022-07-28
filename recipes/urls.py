from turtle import home
from django.contrib import admin
from django.urls import path,include
from .views import home

#Domain.com/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
   
]