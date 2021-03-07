from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.recipe, name="recipe"),
    path('about/', views.home, name="about"),
    path('shopping_list/add/<str:name>', views.add_to_shopping_list, name="shopping_list_add"),
    path('shopping_list/delete/<str:name>', views.delete_from_shopping_list, name="shopping_list_delete"),
    path('shopping_list/', views.shoppinglist, name="shopping_list"),
    path('recipe/<int:recipe_id>', views.recipe_detail, name="recipe_detail"),
    path('recipe/', views.recipe, name="recipe"),
    path('add/', views.create_recipe, name="recipe_item_form"),
    path('update/<int:id>', views.update_recipe_item, name="update-recipe-item"),
    path('delete/<int:id>', views.delete_recipe_item, name="delete_recipe_item"),
    path('print/<int:recipe_id>', views.print_recipe, name="print_recipe"),

]
app_name = 'MyCookbook'

