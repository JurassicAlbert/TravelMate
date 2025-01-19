from rest_framework import serializers
from ..models.travel_location import TravelLocation


class TravelLocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the TravelLocation model.
    """

    recommended_by = serializers.StringRelatedField(many=True, read_only=True)

    # Optionally, use `PrimaryKeyRelatedField` or a custom nested serializer if needed:
    # recommended_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TravelLocation
        fields = ['id', 'name', 'description', 'category', 'latitude', 'longitude', 'recommended_by']
        read_only_fields = ['recommended_by']

    def validate_latitude(self, value):
        """
        Validate the latitude value to ensure it is within the valid range (-90 to 90).
        """
        if value < -90 or value > 90:
            raise serializers.ValidationError("Latitude must be between -90 and 90 degrees.")
        return value

    def validate_longitude(self, value):
        """
        Validate the longitude value to ensure it is within the valid range (-180 to 180).
        """
        if value < -180 or value > 180:
            raise serializers.ValidationError("Longitude must be between -180 and 180 degrees.")
        return value

    def validate_category(self, value):
        """
        Validate that the category matches one of the predefined categories.
        """
        valid_categories = ['attraction', 'restaurant', 'hotel']  # Add other valid categories here
        if value not in valid_categories:
            raise serializers.ValidationError(f"Category must be one of {valid_categories}.")
        return value
