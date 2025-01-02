from rest_framework import serializers
from ..models.travel_history import TravelHistory
from ..models.travel_location import TravelLocation
from ..models.app_user import AppUser


class TravelHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the TravelHistory model.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=TravelLocation.objects.all())

    class Meta:
        model = TravelHistory
        fields = ['id', 'user', 'location', 'visited_at']
        read_only_fields = ['visited_at']
