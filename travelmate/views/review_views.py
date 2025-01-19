from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required

from ..forms.review_form import ReviewForm
from ..models.review import Review


class ReviewView:
    @login_required
    def review_list(request):
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'reviews': reviews})

    @login_required
    def add_review(request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('review_list')
        else:
            form = ReviewForm()
        return render(request, 'add_review.html', {'form': form})

    @login_required
    def edit_review(request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if review.user != request.user:
            raise PermissionDenied("You do not have permission to edit this review.")

        if now() - review.created_at > timedelta(weeks=2):
            raise PermissionDenied("You can only edit your review within two weeks of creation.")

        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('review_list')
        else:
            form = ReviewForm(instance=review)
        return render(request, 'edit_review.html', {'form': form})
