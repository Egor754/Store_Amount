from django.urls import path

from my_shop.views import HomeView, ShopView, ShopViewCategory, DetailProductView, CartView, CheckoutView, FavoriteView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('shop/<slug:slug>', ShopViewCategory.as_view(), name='shop_category'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/product/<slug:slug>', DetailProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/', CartView.as_view(), name='cart'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('favorite', FavoriteView.as_view(), name='favorite'),
]
