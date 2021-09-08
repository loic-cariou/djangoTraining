from .Unit import Unit
from .Recipe import Recipe
from .Ingredient import Ingredient
from django.db import models


class RecipeIngredientUnit(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    value = models.FloatField(default=1, blank=False)
    show_unit = models.BooleanField(default=True, blank=False)

    def __str__(self) -> str:
        title = self.recipe.title + ' : ' + \
            self.ingredient.name_by_value(self.value)
        if(self.show_unit):
            title = title + ' => ' + str(self.value) + ' ' + self.unit.name
        return title
