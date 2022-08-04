from django.test import TestCase
from django.urls import reverse, resolve
from .views import home,category,recipes


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        print('Olá mundo')
        assert 1 == 1, 'Um é igual a um'

    def test_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url,'/')

    def test_category_url_is_correct(self):
        category_url = reverse('recipes:category',kwargs= {'category_id' : 1} )
        self.assertEqual(category_url,'/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        recipe_url = reverse('recipes:recipe', kwargs= {'id':1})
        self.assertEqual(recipe_url, '/recipes/1/')

class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        home_view = resolve(reverse('recipes:home'))
        self.assertIs(home_view.func, home)
    
    def test_recipe_category_views_function_is_correct(self):
        category_view = resolve(reverse('recipes:category', kwargs = {'category_id' : 1}))
        self.assertIs(category_view.func, category)

    def test_recipe_recipes_views_function_is_correct(self):
        recipe_view = resolve(reverse('recipes:recipe', kwargs = {'id' : 1}))
        self.assertIs(recipe_view.func, recipes)
