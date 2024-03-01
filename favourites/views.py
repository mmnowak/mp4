from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Favourites

@login_required
def view_favourites(request):
    """ A view that displays user's favourites """

    all_favourites = Favourites.objects.filter(username=request.user.id)[0]

    favourites_products = all_favourites.products.all()

    template = 'favourites/view_favourites.html'

    context = {
        'favourites_products': favourites_products
    }

    return render(request, template, context)


@login_required
def add_favourite(request, product_id):
    """ Adds a product to user's favourites """

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
    



