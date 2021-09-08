from django.contrib import admin
from .models.Unit import Unit
from .models.RecipeIngredientUnit import RecipeIngredientUnit
from .models.Ingredient import Ingredient
from .models.Recipe import Recipe
from .models.Person import Person
from .models.Phone import Phone
from .models.Address import Address


class RecipeIngredientUnitAdmin(admin.TabularInline):
    model = RecipeIngredientUnit
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientUnitAdmin,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Address)
