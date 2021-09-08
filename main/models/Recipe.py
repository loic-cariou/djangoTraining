from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    summary = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title