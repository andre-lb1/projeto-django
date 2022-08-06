from django.test import TestCase
from recipes.models import Category,Recipes,User


class RecipeTestBase(TestCase):

    # def setUp(self) -> None:
    #     self.make_recipe()
    #     return super().setUp()

    def make_category(self, name = 'Category'):
        return Category.objects.create(name = name)

    def make_author(self, first_name = 'User', last_name = 'Name', 
        username = 'username', password = '123123', email = 'username@gmail.com'):
        return User.objects.create(first_name = first_name, last_name = last_name, 
        username = username, password = password, email = email)
    
    def make_recipe(
        self,
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
        category_data = None,
        author_data = None):
        
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipes.objects.create(
        title = title,
        description = description,
        slug = slug,
        preparation_time = preparation_time,
        preparation_time_unit = preparation_time_unit,
        servings = servings,
        servings_unit = servings_unit,
        preparation_steps = preparation_steps,
        preparation_steps_is_html = preparation_steps_is_html,
        is_published = is_published,
        category = self.make_category(**category_data),
        author = self.make_author(**author_data)
        )
        
