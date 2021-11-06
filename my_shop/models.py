from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    stars = models.PositiveIntegerField(verbose_name='Рейтинг')
    in_stock = models.BooleanField(verbose_name='В наличии')
    in_stock_max = models.PositiveIntegerField(verbose_name='Количество товара на складе')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория товара',
                                 related_name='product')
    brand = models.ForeignKey('Brands', on_delete=models.PROTECT, verbose_name='Бренд', related_name='product')

    def __str__(self):
        return f'Товар {self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Images(models.Model):
    image = models.ImageField(verbose_name='Изображение товара')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def __str__(self):
        return f'Изображение товара {self.product.id}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brands(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название бренда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
