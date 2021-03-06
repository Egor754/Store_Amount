# Generated by Django 3.2.9 on 2021-11-19 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название бренда')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название категории')),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Изображение категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('stars', models.PositiveIntegerField(verbose_name='Рейтинг')),
                ('in_stock', models.BooleanField(verbose_name='В наличии')),
                ('in_stock_max', models.PositiveIntegerField(verbose_name='Количество товара на складе')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('image_base', models.ImageField(upload_to='product_images', verbose_name='Изображение товара')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='my_shop.brands', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='my_shop.categories', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-stars'],
            },
        ),
        migrations.CreateModel(
            name='ImagesHover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images', verbose_name='Изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_hover', to='my_shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение hover',
                'verbose_name_plural': 'Изображения hover',
            },
        ),
    ]
