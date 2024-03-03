from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Favourites

@login_required
def view_favourites(request):
    """ A view that displays user's favourites """

    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourites_products = None
    else:
        favourites_products = all_favourites.products.all()

    if not favourites_products:
        messages.info(request, "You don't haveany favourites yet!")

    template = 'favourites/view_favourites.html'

    context = {
        'favourites_products': favourites_products
    }

    return render(request, template, context)


@login_required
def add_favourite(request, product_id):
    """ Adds a product to user's favourites """

    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you have to log in to add to favourites!')
        return redirect(reverse('product_detail', args=[product_id]))

    product = get_object_or_404(Product, pk=product_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)
    if product in favourites.products.all():
        messages.info(request, 'The product is already in your favourites!')    
    else:
        favourites.products.add(product)
        messages.info(request, 'Added the product to your favourites')
    
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_favourite(request, product_id, redirect_from):
    """ Removes a product from user's favourites """
    product = get_object_or_404(Product, pk=product_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, 'Removed this product '
                               'from your favourites!')
    else:
        messages.error(request, 'This product is '
                                'not in your favourites!')
    if redirect_from == 'favourites':
        redirect_url = reverse('view_favourites')
    else:
        redirect_url = reverse('product_detail', args=[product_id])
    return redirect(redirect_url)


    



