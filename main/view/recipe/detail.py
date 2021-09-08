from django.views.generic import DetailView
from main.models.Recipe import Recipe


class RecipeDetailView(DetailView):
    template_name = 'recipe/detail.html'
    model = Recipe