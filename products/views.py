from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, incluring sorting and search queries """

    products = Product.objects.all()
    query = None
    product_type = None

    if request.GET:
        if 'product_type_name' in request.GET:
            product_type = request.GET['product_type_name'].split(',')
            products = products.filter(category__product_type_name__in=product_type)
            product_type = Category.objects.filter(product_type_name__in=product_type)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(product_name__icontains=query) | Q(ingredients__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_type': product_type,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
    
