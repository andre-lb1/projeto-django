from base64 import decode
from django.urls import resolve, reverse
from recipes.views import category, home, recipes, search
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

    def test_recipe_search_views_is_correct(self):
        response = resolve(reverse('recipes:search'))
        self.assertEqual(response.func, search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=testing')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_q(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code,404)

    def test_recipe_search_term_is_on_title_and_escaped(self):
        response = self.client.get(reverse('recipes:search')  + '?q=<testing term>')
        self.assertIn('Search for &lt;testing term&gt', response.content.decode('utf-8'))

