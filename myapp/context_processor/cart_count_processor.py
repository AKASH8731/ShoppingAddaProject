from cart.models import Cart


def cart_count(request):
    """ context processor for  cart count """
    quantity = 0
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        for cart in carts:
            quantity = quantity + cart.quantity
    return {'global_cart_quantity': quantity}
