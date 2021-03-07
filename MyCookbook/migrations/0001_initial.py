# Generated by Django 2.2 on 2020-12-07 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('checked_out', models.BooleanField(default=False, verbose_name='checked out')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'ordering': ('-creation_date',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='profilepic.jpg', upload_to='pictures')),
                ('instructions', models.TextField(default='Mix all ingredients')),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField(default='1.00', max_length=255)),
                ('unit', models.CharField(default='Cups', max_length=255)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyCookbook.Cart', verbose_name='cart')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='MyCookbook.Recipe')),
            ],
            options={
                'db_table': 'ingredient',
            },
        ),
    ]
