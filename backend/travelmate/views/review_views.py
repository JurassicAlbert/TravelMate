from datetime import timedelta
from django.utils.timezone import now
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models.review import Review
from ..serializers.review_serializer import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    """
    ViewSet for handling Review CRUD operations with restrictions.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the logged-in user when creating a review.
        """
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        Allow users to update their review only within two weeks of creation.
        """
        instance = self.get_object()

        # Check if the logged-in user is the review's author
        if instance.user != request.user:
            raise PermissionDenied("You do not have permission to edit this review.")

        # Check if the review is older than two weeks
        if now() - instance.created_at > timedelta(weeks=2):
            raise PermissionDenied("You can only edit your review within two weeks of creation.")

        return super().update(request, *args, **kwargs)
