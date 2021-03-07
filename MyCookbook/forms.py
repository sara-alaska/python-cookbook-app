from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import Recipe, Ingredient, ShoppingList

CATEGORY_CHOICES = (
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
    ("Vegan", "Vegan"),
    ("Vegetarian", "Vegetarian"),
    ("Dessert", "Dessert")
)


UNIT_CHOICES = (
    ("Teaspoons", "Teaspoons"),
    ("Tablespoons", "Tablespoons"),
    ("Cups", "Cups"),
    ("Whole", "Whole"),
    ("Half", "Half"),
    ("Grams", "Grams")
)


class RecipeForm(forms.Form):
    name = forms.CharField(
        label='Recipe Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
    ),
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'image', 'instructions', 'category')
        labels = {
            'name': 'Recipe Name',
            'image': 'Recipe Image',
            'instructions': 'Recipe Instructions',
            'category': 'Recipe Category'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Recipe Name'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=CATEGORY_CHOICES)
        }


IngredientFormset = modelformset_factory(
    Ingredient,
    fields=('name', 'amount', 'unit'),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingredient Name'
    }),
        'amount': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount'
        }),
        'unit': forms.Select(attrs={'class': 'form-control'}, choices=UNIT_CHOICES)
    }
)


class ShoppingListForm(forms.Form):
    class Meta:
        model = ShoppingList
        fields = 'list_item'

        widgets = {
            'list_item': forms.HiddenInput(attrs={'class': 'form-control'})
        }