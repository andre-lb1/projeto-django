from base64 import decode
from django.urls import resolve, reverse
from recipes.views import category
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):
    def test_recipe_category_views_function_is_correct(self):
        category_view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(category_view.func, category)

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'test recipe'
        recipe = self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category', kwargs={
                                   'category_id': recipe.category_id}))
        self.assertIn(needed_title, response.content.decode('utf-8'))

    def test_recipe_category_template_dont_show_not_published_recipes(self):
        needed_title = 'Test not published recipes'
        recipe = self.make_recipe(title=needed_title, is_published=False)
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': recipe.category_id}))
        self.assertNotIn(needed_title, response.content.decode('utf-8'))
