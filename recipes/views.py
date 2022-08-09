from turtle import title
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from recipes.models import Recipes
from django.db.models import Q


def home(request):
    recipes = Recipes.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', {'recipes': recipes})


def category(request, category_id):
    # recipes = Recipes.objects.filter(category__id = category_id).order_by('-id')#__nome do campo do model de onde vem
    # a foreignkey
    recipes = get_list_or_404(Recipes.objects.filter(
        category_id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/category.html', {'recipes': recipes, 'category_name': f'Category - {recipes[0].category.name} │'})


def recipes(request, id):
    recipe = get_object_or_404(Recipes.objects.filter(id = id, is_published = True))
    return render(request, 'recipes/pages/recipe-view.html', {'recipe': recipe, 'is_detail_page': True})

def search(request):
    search_term = request.GET.get('q','').strip() # --> return None if 'q' is null or space(s).
    if not search_term:
        raise Http404()

    recipes = Recipes.objects.filter(
        Q(title__icontains = search_term) |
        Q(description__icontains = search_term),
        is_published = True
        ).order_by('-id') # --> SELECT * FROM recipes_recipes WHERE title LIKE %search_term% 
                                #OR description LIKE %search_term%

    return render(request, 'recipes/pages/search.html', 
    context = {'recipes':recipes, 'page_title' : f'Search for {search_term} │', 
    'search_term' : search_term})