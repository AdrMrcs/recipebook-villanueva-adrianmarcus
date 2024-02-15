from django.urls import path

from .views import index, recipe_list

urlpatterns = [
    path('', index, name="index"),
    path('recipes', recipe_list, name="recipes"),

]

app_name = "ledger"