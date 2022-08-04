from django.shortcuts import render,get_list_or_404,get_object_or_404
from utils.recipes.random_recipes import make_recipe
from .models import Recipes, Category
from django.http import Http404

def home(request):
    recipes = Recipes.objects.filter(is_published = True).order_by('-id')
    return render(request,'recipes/pages/home.html',{'recipes' : recipes})

def category(request,category_id):
    # recipes = Recipes.objects.filter(category__id = category_id).order_by('-id')#__nome do campo do model de onde vem
    #a foreignkey
    recipes = get_list_or_404(Recipes.objects.filter(category_id = category_id, is_published = True).order_by('-id'))
    return render(request,'recipes/pages/category.html',{'recipes' : recipes, 'category_name': f'Category - {recipes[0].category.name} │'})
    
def recipes(request,id):
    return render(request,'recipes/pages/recipe-view.html',{'recipe' : make_recipe(),'is_detail_page':True})





