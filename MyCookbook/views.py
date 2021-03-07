import pdfkit as pdfkit
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import RecipeModelForm, IngredientFormset, ShoppingListForm
from .models import Recipe, Ingredient, ShoppingList
import io


def create_recipe(request):
    template_name = 'MyCookbook/recipe_item_form.html'
    if request.method == 'GET':
        recipeform = RecipeModelForm(request.GET or None)
        formset_ingredients = IngredientFormset(queryset=Ingredient.objects.none())

    elif request.method == 'POST':
        recipeform = RecipeModelForm(data=request.POST, files=request.FILES)
        formset_ingredients = IngredientFormset(request.POST)

        if recipeform.is_valid() and formset_ingredients.is_valid():
            recipe = recipeform.save()
            for form in formset_ingredients:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()

            return redirect('MyCookbook:recipe')
    return render(request, template_name, {
        'recipeform': recipeform,
        'formset_ingredients': formset_ingredients

    })


def home(request):
    return render(request, 'MyCookbook/about.html')


def add_to_shopping_list(request, name):
    shopping_list = ShoppingList.objects.create(list_item=name)
    shopping_list.save()

    return shoppinglist(request)


def delete_from_shopping_list(request, name):
    shopping_list = ShoppingList.objects.get(list_item=name)
    shopping_list.delete()

    return shoppinglist(request)


def shoppinglist(request):
    shopping_list = ShoppingList.objects.all()
    context = {
        'shopping_list': shopping_list,
    }
    return render(request, 'MyCookbook/shopping_list.html', context)


def recipe(request):
    recipe_list = Recipe.objects.all()
    recipe_name = request.GET.get('name')
    if recipe_name != '' and recipe_name is not None:
        recipe_list = recipe_list.filter(name__icontains=recipe_name)
    context = {
        'recipe_list': recipe_list,
    }
    return render(request, 'MyCookbook/recipe.html', context)


def recipe_detail(request, recipe_id):
    item = Recipe.objects.get(pk=recipe_id)
    context = {
        'recipe': item
    }
    return render(request, 'MyCookbook/recipe_detail.html', context)


def update_recipe_item(request, id):
    recipe_obj = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = RecipeModelForm(request.POST or None, request.FILES or None, instance=recipe_obj)
        if form.is_valid():
            form.save()
            return redirect('MyCookbook:recipe')
    else:
        # Prepopulation happens here:
        data = {
            "name": recipe_obj.name,
            "image": recipe_obj.image,
            "instructions": recipe_obj.instructions,
            "category": recipe_obj.category,
            "ingredients": recipe_obj.get_ingredients()
        }

        form = RecipeModelForm(initial=data)

    context = {'form': form}
    return render(request, 'MyCookbook/edit_recipe.html', context)


def delete_recipe_item(request, id):
    item = Recipe.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('MyCookbook:recipe')

    return render(request, 'MyCookbook/recipe_item_delete.html', {'item': item})


def print_recipe(request, recipe_id):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    recipe_obj = Recipe.objects.get(pk=recipe_id)
    template = loader.get_template('MyCookbook/print_recipe.html')
    html = template.render({'recipe': recipe_obj})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = 'attachment'
    filename = "recipe.pdf"

    return response


