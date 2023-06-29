from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Cart
from django.contrib.auth.decorators import login_required
from product.models import Product
from .forms import PlaceOrderForm
from order.models import Order, OrderDetails
from datetime import datetime


@login_required
def add_to_cart_view(request):
    """ Handle add to cart """
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        variation_id = request.POST.get('variation_id')
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        cart, is_created = Cart.objects.get_or_create(
            user=request.user, product_id=product_id, variation_id=variation_id)
        cart.quantity = quantity
        cart.save()

        return redirect('ProductDetails', product_slug=product.slug)
    return redirect('home_page')


@login_required
def my_cart_view(request):
    """ Display list of products in cart """
    cart_products = Cart.objects.filter(user=request.user)
    sub_total = 0
    shipping = 50
    for cart_product in cart_products:
        cart_product.sub_total = cart_product.product.price * cart_product.quantity
        sub_total = sub_total + cart_product.sub_total
    grand_total = sub_total + shipping
    context = {
        'cart_products': cart_products,
        'sub_total': sub_total,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'cart/my_cart.html', context)


@login_required
def delete_cart_item_view(request, cart_id):
    """ Delete an item from my cart """
    try:
        Cart.objects.get(id=cart_id).delete()
    except Cart.DoesNotExist:
        pass
    return redirect('my_cart_view')


@login_required
def checkout(request):
    initial = {
        'address': request.user.user_detail.address,
        'mobile': request.user.user_detail.mobile,
    }
    form = PlaceOrderForm(request.POST or None, initial=initial)
    cart_products = Cart.objects.filter(user=request.user)
    sub_total = 0
    shipping = 50
    for cart_product in cart_products:
        cart_product.sub_total = cart_product.product.price * cart_product.quantity
        sub_total = sub_total + cart_product.sub_total
    grand_total = sub_total + shipping

    """ Proceed to checkout """
    if request.method == "POST":
        """ Form Handling """
        if form.is_valid():
            mobile = form.cleaned_data.get('mobile')
            address = form.cleaned_data.get('address')
            order = Order.objects.create(
                user=request.user,
                date_time=datetime.now(),
                address=address,
                mobile=mobile,
            )
            for cart_product in cart_products:
                """ Processing cart to create order details """
                OrderDetails.objects.create(
                    order=order,
                    product=cart_product.product,
                    quantity=cart_product.quantity,
                    price=cart_product.product.price,
                    variation=cart_product.variation,
                )
            cart_products.delete()
            return redirect('thank_you_view')

    context = {
        'form': form,
        'sub_total': sub_total,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'cart/chekout.html', context)


def thank_you_view(request):
    return render(request, 'cart/thankyou.html')


# @login_required
# def checkout(request):
#     if request.method == "POST":
#         pass

#     return render(request, 'cart/chekout.html')
