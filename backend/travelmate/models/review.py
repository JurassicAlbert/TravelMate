from django.db import models
from .app_user import AppUser
from .travel_location import TravelLocation


class Review(models.Model):
    """
    Model representing a user's review of a travel location.
    Includes a description, rating, and optional photo uploads.
    """
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text="The user who left the review."
    )
    location = models.ForeignKey(
        TravelLocation,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text="The travel location being reviewed."
    )
    description = models.TextField(
        blank=True,
        help_text="The user's review description."
    )
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        help_text="Rating of the location (1 to 5)."
    )
    photos = models.ImageField(
        upload_to='review_photos/',
        blank=True,
        null=True,
        help_text="Optional photo upload related to the review."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time the review was created."
    )

    def __str__(self):
        return f"Review by {self.user.email} for {self.location.name} - Rating: {self.rating}"
