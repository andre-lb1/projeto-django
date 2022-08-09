from base64 import decode
from django.urls import resolve, reverse
from recipes.views import home
from .test_recipe_base import RecipeTestBase



class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_views_function_is_correct(self):
        home_view = resolve(reverse('recipes:home'))
        self.assertIs(home_view.func, home)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertInHTML('No recipes found here.',
                          response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        needed_title = 'Testing if home template loads recipes'
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:home'))
        # response_context = response.context['recipes']
        # self.assertEqual(response_context.first().title, 'recipe title')
        self.assertIn(needed_title, response.content.decode('utf-8'))
        self.assertIn('5 min', response.content.decode('utf-8'))
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_template_dont_show_not_published_recipes(self):
        needed_title = 'Testing if home template shows just published recipes'
        self.make_recipe(is_published=False, title=needed_title)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here.',
                      response.content.decode('utf-8'))
        self.assertNotIn(needed_title, response.content.decode('utf-8'))