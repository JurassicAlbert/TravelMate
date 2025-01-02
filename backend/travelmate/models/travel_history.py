from django.db import models
from .travel_location import TravelLocation
from .app_user import AppUser  # Import the custom AppUser model


class TravelHistory(models.Model):
    """
    Model representing an app user's travel history.
    Links app users with the locations they have visited and records visit details.
    """
    user = models.ForeignKey(
        AppUser,  # Use the custom AppUser model
        on_delete=models.CASCADE,
        related_name='travel_history',
        help_text="The app user associated with this travel history record."
    )
    location = models.ForeignKey(
        TravelLocation,
        on_delete=models.CASCADE,
        related_name='visit_history',
        help_text="The travel location associated with this record."
    )
    visited_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the location was visited."
    )

    def __str__(self):
        return f"{self.user.email} visited {self.location.name} on {self.visited_at}"
