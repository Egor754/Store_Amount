from django.db.models import Min, Prefetch
from django.shortcuts import get_list_or_404, redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from my_shop.cart import Cart
from my_shop.models import Categories, Product, Brands
from my_shop.utils import MixinShopView


class HomeView(ListView):
    template_name = 'my_shop/index.html'
    context_object_name = 'categories'
    model = Categories

    def get_queryset(self):
        print(self.request.session['cart'])
        return Categories.objects.prefetch_related('product').annotate(min_price=Min('product__price'))


class ShopView(MixinShopView, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        c_def = self.get_context_shop()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        brands = self.request.GET.getlist('brand')
        if brands:
            all_products = Product.objects.prefetch_related('image_hover').filter(
                brand__slug__in=brands)
        else:
            all_products = Product.objects.prefetch_related('image_hover')
        return all_products


class ShopViewCategory(ShopView):
    def get_queryset(self):
        brands = self.request.GET.getlist('brand')
        if brands:
            all_products = Product.objects.prefetch_related('image_hover').filter(
                brand__slug__in=brands, category__slug=self.kwargs['slug'])
        else:
            all_products = get_list_or_404(Product.objects.prefetch_related('image_hover'),
                                           category__slug=self.kwargs['slug'])
        return all_products


class DetailProductView(ListView):
    model = Product
    template_name = 'my_shop/product-details.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.prefetch_related('image_hover').get(pk=self.kwargs['slug'])

    def post(self, request, slug, *args, **kwargs):
        data = request.POST
        cart = Cart(request)
        product = get_object_or_404(Product, id=slug)
        cart.add(product=product,
                 quantity=data['quantity']
                 )
        return redirect('cart')


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, 'my_shop/cart.html', {'cart': cart})
