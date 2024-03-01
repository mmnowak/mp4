from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from .forms import ProductForm
from checkout.models import OrderLineItem
from favourites.models import Favourites


# Create your views here.

def all_products(request):
    """ A view to show all products, incluring sorting and search queries """

    products = Product.objects.all()

    query = None
    product_type = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('product_name'))
            if sortkey == 'category':
                sortkey = 'category__product_type_name'
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)
                

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_type': product_type,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display individual product details """

    product = get_object_or_404(Product, pk=product_id)

    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        in_favourites = False
    else:
        in_favourites = bool(product in favourites.products.all())

    context = {
        'product': product,
        'in_favourites': in_favourites
    }

    return render(request, 'products/product_detail.html', context)

@login_required   
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # Checks if product is in cart

    lineitems = OrderLineItem.objects.all()

    for lineitem in lineitems:
        if product == lineitem.product:
            cart = request.session.get('cart', {})
            if product_id in cart:
                cart.pop(product_id)

                # Updates cart in session
                request.session['cart'] = cart

                # messages.success(request, 'Product deleted!')
                # request.session['view_cart'] = True

                # product.delete()
                # messages.success(request, 'Product deleted!')
                return redirect(reverse('products'))
        else:
            product.delete()
            messages.success(request, 'Product deleted!')
            return redirect(reverse('products'))