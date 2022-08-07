from recipes.tests.test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes.models import Recipes


class RecipeTestModels(RecipeTestBase):

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        return Recipes.objects.create(
        title = 'recipe title',
        description = 'desc',
        slug = 'recipe-test',
        preparation_time = '5',
        preparation_time_unit = 'min',
        servings = '1',
        servings_unit = 'recipe unit serving',
        preparation_steps = 'steps for prepairing recipe',
        author = self.make_author(username = 'Recipe test author'),
        category = self.make_category(name = 'Category test name')
        )


    @parameterized.expand([
            ('title' , 65),
            ('description' , 165),
            ('preparation_time_unit' , 65),
            ('servings_unit' , 65),
        ])

    def test_recipe_fields_max_lenght(self, field, max_lenght):
                setattr(self.recipe, field, 'A'*(max_lenght + 1))
                with self.assertRaises(ValidationError):
                    self.recipe.full_clean()

    def test_recipe_preparation_steps_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html, 
        msg = 'preparation_steps_is_html is not False.')

    def test_recipe_is_published_is_False_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published, msg= 'is_published is not False.')

    def test_recipe_string_representation(self):
        needed_title = 'test recipe title str'
        self.recipe.title = needed_title
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed_title, 
        msg = f'recipe string representation must be {needed_title}, but ' \
              f'"{str(self.recipe)}" was received')
