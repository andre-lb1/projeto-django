from turtle import home
from django.contrib import admin
from django.urls import path,include
from . import views

#Domain.com/

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipes'),
   
]