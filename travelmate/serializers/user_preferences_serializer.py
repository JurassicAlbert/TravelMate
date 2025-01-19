from rest_framework import serializers
from ..models.user_preferences import UserPreferences
from ..models.app_user import AppUser


class UserPreferencesSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserPreferences model.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = UserPreferences
        fields = ['id', 'user', 'prefers_category']
