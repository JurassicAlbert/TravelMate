from django.db import models
from .app_user import AppUser  # Import the custom AppUser model


class TravelLocation(models.Model):
    """
    Model representing a travel location.
    Includes details about the name, description, category, and geolocation.
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

    name = models.CharField(
        max_length=255,
        help_text="Name of the location."
    )
    description = models.TextField(
        blank=True,
        help_text="Description of the location."
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        help_text="Category of the location."
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Latitude of the location."
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude of the location."
    )
    recommended_by = models.ManyToManyField(
        AppUser,  # Use the custom AppUser model
        related_name='recommended_locations',
        blank=True,
        help_text="App users who recommended this location."
    )

    def __str__(self):
        return self.name
