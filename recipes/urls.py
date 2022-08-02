from turtle import home
from django.contrib import admin
from django.urls import path,include
from . import views

#Domain.com/
app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
   
]