from rest_framework import serializers
from ..models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """

    class Meta:
        model = Review
        fields = ['id', 'user', 'location', 'description', 'rating', 'photos', 'created_at']
        read_only_fields = ['created_at']
