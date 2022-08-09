from base64 import decode
from django.urls import resolve, reverse
from recipes.views import recipes
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_recipes_views_function_is_correct(self):
        recipe_view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(recipe_view.func, recipes)

    def test_recipes_view_return_404_if_no_recipe_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It loads a unique recipe'
        recipe = self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id}))
        self.assertIn(needed_title, response.content.decode('utf-8'))

    def test_recipe_detail_page_not_show_unpublished_recipes(self):
        needed_title = 'Testing detail page with unpublished contents'
        self.make_recipe(title=needed_title, is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
        self.assertNotIn(needed_title, response.content.decode('utf-8'))