from django.shortcuts import render
from utils.recipes.random_recipes import make_recipe

def home(request):
    return render(request,'recipes/pages/home.html',{'recipes' : [make_recipe() for _ in range(10)]})

def recipes(request,id):
    return render(request,'recipes/pages/recipe-view.html',{'recipe' : make_recipe(),'is_detail_page':True})





