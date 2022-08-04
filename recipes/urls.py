from turtle import home

from django.urls import include, path

from . import views

# Domain.com/
app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
]
