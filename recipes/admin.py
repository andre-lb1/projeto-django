from django.contrib import admin
from .models import Category,Recipes

class CategoryAdmin(admin.ModelAdmin):
    ...
class RecipesAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipes,RecipesAdmin)

