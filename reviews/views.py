from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile

def reviews(request, product_id):
    """ A view to show all existing reviews for a product """
    product = get_object_or_404(Product, pk=product_id)

    reviews = Review.objects.filter(product=product)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'product': product,
    }

    return render(request, template, context)


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

            avg_rating = round(Review.objects.aggregate(Avg('rating'))['rating__avg'])
            product.rating = avg_rating
            product.save()

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

@login_required()
def edit_review(request, review_id):
    """
    Renders an edit review form for logged in users
    Updates review in db
    """

    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to log in to edit a review!')
        return redirect(reverse('account_login'))

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(review=review)[0]

    if request.user != review.user:
        messages.error(request, 'You can only edit your own reviews.')
        return redirect(reverse('reviews', args=[product.id]))

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save()
            review.save()

            redirect_url = request.POST.get('redirect_url')

            avg_rating = round(Review.objects.aggregate(Avg('rating'))['rating__avg'])
            product.rating = avg_rating
            product.save()

            messages.success(request, f'You successfully updated your review!')
            return redirect(reverse('reviews', args=[product.id]))
        else:
            messages.error(request, f'Your form is invalid')
    
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review titled: "{review.title}"')

    template = 'reviews/edit_review.html'


    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)
    



