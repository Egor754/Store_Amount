from PIL import Image
from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

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
    date_add = models.DateField(verbose_name='Время добавления', auto_now_add=True)

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


COUNTRY_CHOICES = [
    ('USA', 'United States'),
    ('UK', 'United Kingdom'),
    ('GERM', 'Germany'),
    ('FR', 'France'),
    ('IND', 'India'),
    ('AUST', 'Australia'),
    ('BR', 'Brazil'),
    ('CAN', 'Canada'),
]


class Orders(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=255, verbose_name='Страна', choices=COUNTRY_CHOICES)
    address = models.TextField(verbose_name='Адрес')
    town = models.CharField(max_length=255, verbose_name='Город')
    zip_code = models.PositiveIntegerField(verbose_name='Почтовый индекс')
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    comment = models.TextField(verbose_name='Коментарий', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    paid = models.BooleanField(default=False, verbose_name='Отправлено')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
