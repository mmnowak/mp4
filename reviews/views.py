from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile

# Create your views here.

@login_required()
def add_review(request, product_id):
    """ 
    Renders a review form for logged in uses 
    Adds a new form to the database
    """

    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to log in to add a review!')
        return redirect(reverse('account_login'))

    product = get_object_or_404(Product, pk=product_id)
    username = User.objects.get(username=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = username
            review.save()
            messages.success(request, "Thank you for adding a new review!")

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()
    
    template = 'reviews/add_review.html'

    context = {
        'review_form': review_form,
        'product': product,
    }

    return render(request, template, context)
