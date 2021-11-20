from PIL import Image
from django.db import models
from django.utils.text import slugify

from shop.settings import MEDIA_PRODUCT_IMAGE_DIR, MEDIA_CATEGORIES_IMAGE_DIR


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    stars = models.FloatField(verbose_name='Рейтинг')
    in_stock = models.BooleanField(verbose_name='В наличии')
    in_stock_max = models.PositiveIntegerField(verbose_name='Количество товара на складе')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория товара',
                                 related_name='product')
    brand = models.ForeignKey('Brands', on_delete=models.PROTECT, verbose_name='Бренд', related_name='product')
    image_base = models.ImageField(verbose_name='Изображение товара', upload_to=MEDIA_PRODUCT_IMAGE_DIR)

    def __str__(self):
        return f'Товар {self.title}'

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        if self.image_base:
            filepath = self.image_base.path
            image = Image.open(filepath)
            image = image.resize((723, 747), Image.ANTIALIAS)
            image.save(filepath)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-stars']


class ImagesHover(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='image_hover')
    image = models.ImageField(upload_to=MEDIA_PRODUCT_IMAGE_DIR, verbose_name='Изображение товара')

    def __str__(self):
        return f'Hover img товара {self.product.id}'

    class Meta:
        verbose_name = 'Изображение hover'
        verbose_name_plural = 'Изображения hover'

    def save(self, *args, **kwargs):
        super(ImagesHover, self).save(*args, **kwargs)

        # Проверяем, указан ли логотип
        if self.image:
            filepath = self.image.path
            image = Image.open(filepath)
            image = image.resize((723, 747), Image.ANTIALIAS)
            image.save(filepath)


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории', unique=True)
    image = models.ImageField(upload_to=MEDIA_CATEGORIES_IMAGE_DIR, verbose_name='Изображение категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brands(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название бренда', unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Brands, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
