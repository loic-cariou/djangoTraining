from django.db.models.query import QuerySet
from django.views.generic import ListView
from main.models.Recipe import Recipe

class RecipeListView(ListView):
    template_name = 'recipe/list.html'

    def get_queryset(self) -> QuerySet[Recipe]:
        return Recipe.objects.all().order_by()