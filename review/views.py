from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_review(request):
    """
    Create a view that will return a list
    of Reviews that were published prior to 'now'
    and render them to the 'reviewposts.html' template
    """
    products = Product.objects.all()
    review = Review.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(
        request, "reviewposts.html", {'review': review, 'products': products})


def review_detail(request, pk_review):
    """
    Create a view that returns a single
    Review object based on the review ID (pk) and
    render it to the 'reviewdetail.html' template.
    Or return a 404 error if the review is not found
    """
    review = get_object_or_404(Review, pk=pk_review)
    review.views += 1
    review.save()
    return render(request, "reviewdetail.html", {'review': review})


@login_required
def create_or_edit_review(request, pk_review=None):
    """
    Create a view that allows us to create
    or edit a review depending if the Review ID
    is null or not
    """
    review = get_object_or_404(Review, pk=pk_review) if pk_review else None
    if request.method == "POST":
        reviewform = ReviewForm(request.POST, request.FILES, instance=review)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect(review_detail, review.pk)
    else:
        reviewform = ReviewForm(instance=review)
    return render(request, 'reviewform.html', {'review_form': reviewform})


@login_required
def delete_review(request, pk_review):
    review = get_object_or_404(Review, pk=pk_review)
    review.delete()
    messages.success(
        request, "Your review has been successfully deleted",
        extra_tags='alert-success')
    return HttpResponseRedirect('/')
