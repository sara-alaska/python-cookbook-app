from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pictures',
                              default='recipe_placeholder.jpg')
    instructions = models.TextField(default='Enter Instructions')
    category = models.CharField(max_length=255)

    class Meta:
        db_table = 'recipe'

    def __str__(self):
        return self.name

    def get_ingredients(self):
        products = list(self.ingredients.filter().values_list('name', 'amount', 'unit'))
        # mapped = set(products)
        return products


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField(max_length=255, default="1.00")
    unit = models.CharField(max_length=255, default="Cups")

    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients', on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'ingredient'

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    list_item = models.CharField(max_length=255)

    class Meta:
        db_table = 'shoppinglist'

    def __str__(self):
        return self.list_item
