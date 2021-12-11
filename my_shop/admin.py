from django.contrib import admin
from my_shop.models import Product, Brands, Categories, ImagesHover, Orders

admin.site.register(Product)
admin.site.register(Brands)
admin.site.register(Categories)
admin.site.register(ImagesHover)
admin.site.register(Orders)
