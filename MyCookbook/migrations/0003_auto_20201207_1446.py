# Generated by Django 2.2 on 2020-12-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCookbook', '0002_remove_ingredient_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]