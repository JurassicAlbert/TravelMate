from django.db import models

from .app_user import AppUser  # Import the custom AppUser model


class UserPreferences(models.Model):
    """
    Model for storing user-specific travel preferences.
    Helps in customizing recommendations based on user interests.
    """
    CATEGORY_CHOICES = [
        ('attraction', 'Attraction'),
        ('restaurant', 'Restaurant'),
        ('hotel', 'Hotel'),
        ('park', 'Park'),
        ('museum', 'Museum'),
        ('beach', 'Beach'),
        ('shopping', 'Shopping Center'),
        ('historical', 'Historical Site'),
        ('nightlife', 'Nightlife Spot'),
        ('nature', 'Natural Reserve'),
        ('adventure', 'Adventure Activity'),
        ('cultural', 'Cultural Experience'),
    ]

    user = models.OneToOneField(
        AppUser,  # Use the custom AppUser model
        on_delete=models.CASCADE,
        related_name='preferences',
        help_text="The app user associated with these preferences."
    )
    prefers_category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        blank=True,
        help_text="Preferred category of travel locations."
    )

    def __str__(self):
        return f"Preferences of {self.user.email}"  # Using email since AppUser doesn't have username
