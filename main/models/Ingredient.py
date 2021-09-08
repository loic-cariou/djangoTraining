from django.db import models


class Ingredient(models.Model):
    name_singular = models.CharField(max_length=200, null=False, blank=False)
    name_plural = models.CharField(max_length=200, null=False, blank=False)

    def name_by_value(self, value: float):
        if(value > 1.0):
            return self.name_plural
        return self.name_singular

    def __str__(self) -> str:
        return self.name_singular
