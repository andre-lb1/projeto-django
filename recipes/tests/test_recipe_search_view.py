from base64 import decode
from turtle import title
from django.urls import resolve, reverse
from recipes.views import search
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_search_views_is_correct(self):
        response = resolve(reverse('recipes:search'))
        self.assertEqual(response.func, search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse( '?q=testing'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_q(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code,404)

    def test_recipe_search_term_is_on_title_and_escaped(self):
        response = self.client.get(reverse('recipes:search')  + '?q=<testing term>')
        self.assertIn('Search for &lt;testing term&gt', response.content.decode('utf-8'))

    def test_recipe_search_can_find_recipes_by_title(self):
        title1 = 'recipe test one'
        title2 = 'recipe test two'
        self.make_recipe(title = title1, slug = 'slug-one', author_data = {'username':'user1'})
        self.make_recipe(title = title2, slug = 'slug-two', author_data = {'username':'user2'})
        
        search_url = reverse('recipes:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=recipe test')
        self.assertIn(title1, response1.content.decode('utf-8'))
        self.assertNotIn(title2, response1.content.decode('utf8'))

        self.assertIn(title2, response2.content.decode('utf-8'))
        self.assertNotIn(title1, response2.content.decode('utf8'))

        self.assertIn(title1, response_both.content.decode('utf-8'))
        self.assertIn(title2, response_both.content.decode('utf-8'))
        
