from my_shop.models import Product, Categories, Brands


class MixinShopView:
    paginate_by = 6
    template_name = 'my_shop/shop.html'
    context_object_name = 'products'
    model = Product

    def get_context_shop(self, **kwargs):
        context = kwargs
        context['categories'] = Categories.objects.all()
        context['brands'] = Brands.objects.all()
        return context
