from my_shop.cart import Cart


def quantity_cart(request):
    return {'qty_cart': len(Cart(request))}
