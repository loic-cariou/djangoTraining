"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main.view.recipe.list import RecipeListView
from main.view.recipe.detail import RecipeDetailView
from main.view.recipe.create import RecipeCreateView
from main.view.index import IndexView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('recipes', RecipeListView.as_view() , name="recipe_list"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe', RecipeCreateView.as_view(), name="recipe_create")
]
