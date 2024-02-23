from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view to return the shopping cart """
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

# Code to ensure the session keeps the right type
    if type(cart) != dict:
        cart = {}

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request, f'Updated {product.product_name} quantity to {cart[product_id]}')
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {product.product_name} to your cart')

    
    request.session['cart'] = cart    
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """ Adjust quantity of the specified product in the shopping cart """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
        messages.success(request, f'Updated {product.product_name} quantity to {cart[product_id]}')
    else:
        cart.pop(product_id)
        messages.success(request, f'Removed {product.product_name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def remove_from_cart(request, product_id):
    """ Removes the specified product from the shopping cart """
    product = get_object_or_404(Product, pk=product_id)

    try:
        cart = request.session.get('cart', {})

        cart.pop(product_id)
        messages.success(request, f'Removed {product.product_name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:        
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)