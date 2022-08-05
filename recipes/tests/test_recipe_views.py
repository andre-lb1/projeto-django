from base64 import decode
from django.test import TestCase
from django.urls import reverse, resolve
from recipes.views import home,category,recipes
from recipes.models import Category,Recipes,User


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        home_view = resolve(reverse('recipes:home'))
        self.assertIs(home_view.func, home)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response,'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertInHTML('No recipes found here.', response.content.decode('utf-8'))

    def test_recipe_home_template_load_recipes(self):
        category = Category.objects.create(name = 'Category')
        author = User.objects.create(
            first_name = 'Danyel', last_name = 'Sena', 
            username = 'mucalol', password = 123123, email = 'smurfdomuca@gmail.com'
            )
        recipe = Recipes.objects.create(
            title = 'recipe title',
            description = 'desc',
            slug = 'recipe-test',
            preparation_time = '5',
            preparation_time_unit = 'min',
            servings = '1',
            servings_unit = 'recipe unit serving',
            preparation_steps = '2',
            preparation_steps_is_html = False,
            is_published = True,
            category = category,
            author = author
        )
        response = self.client.get(reverse('recipes:home'))
        # response_context = response.context['recipes']
        # self.assertEqual(response_context.first().title, 'recipe title')
        self.assertIn('recipe title', response.content.decode('utf-8'))


    def test_recipe_category_views_function_is_correct(self):
        category_view = resolve(reverse('recipes:category', kwargs = {'category_id' : 1}))
        self.assertIs(category_view.func, category)

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs= {'category_id' : 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipes_views_function_is_correct(self):
        recipe_view = resolve(reverse('recipes:recipe', kwargs = {'id' : 1}))
        self.assertIs(recipe_view.func, recipes)

    def test_recipes_view_return_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs= {'id':1000}))
        self.assertEqual(response.status_code, 404)

    