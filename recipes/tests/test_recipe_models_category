from recipes.tests.test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeTestModels(RecipeTestBase):

    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()

    def test_recipe_category_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_recipe_category_model_name_max_lenght(self):
        self.category.name = 'A'*70
        with self.assertRaises(ValidationError):
            self.category.full_clean()