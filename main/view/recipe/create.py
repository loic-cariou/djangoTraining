from main.forms.Recipe import RecipeForm
from django.views.generic import CreateView
from main.models.Recipe import Recipe


class RecipeCreateView(CreateView):
    template_name = 'recipe/create.html'
    model = Recipe
    fields = ('title', 'content')
