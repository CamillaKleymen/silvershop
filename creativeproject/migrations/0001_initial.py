# Generated by Django 5.0.4 on 2024-04-21 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(help_text='here you should enter name of product', max_length=50)),
                ('product_price', models.FloatField()),
                ('product_count', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_image', models.FileField(upload_to='product_images')),
                ('product_created_at', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creativeproject.categorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_quantity', models.IntegerField()),
                ('user_add_date', models.DateTimeField(auto_now_add=True)),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creativeproject.productmodel')),
            ],
            options={
                'verbose_name': 'User cart',
                'verbose_name_plural': 'User carts',
            },
        ),
    ]
