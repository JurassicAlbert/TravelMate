from rest_framework import serializers
from ..models.travel_location import TravelLocation


class TravelLocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the TravelLocation model.
    """

    class Meta:
        model = TravelLocation
        fields = ['id', 'name', 'description', 'category', 'latitude', 'longitude', 'recommended_by']
        read_only_fields = ['recommended_by']
