from django.contrib import admin
from my_shop.models import Product, Images, Brands, Categories

admin.site.register(Product)
admin.site.register(Brands)
admin.site.register(Categories)
admin.site.register(Images)
