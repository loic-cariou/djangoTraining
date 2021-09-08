from django.contrib import admin
from .models.Unit import Unit
from .models.RecipeIngredientUnit import RecipeIngredientUnit
from .models.Ingredient import Ingredient
from .models.Recipe import Recipe


class RecipeIngredientUnitAdmin(admin.TabularInline):
    model = RecipeIngredientUnit
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientUnitAdmin,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
