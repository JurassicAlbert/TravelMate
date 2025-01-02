from rest_framework import serializers
from ..models.app_user import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the AppUser model.
    """
    password = serializers.CharField(write_only=True, min_length=8, help_text="Password for the user account.")

    class Meta:
        model = AppUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'is_active', 'date_joined']
        read_only_fields = ['is_active', 'date_joined']

    def create(self, validated_data):
        """
        Override the create method to securely hash passwords.
        """
        password = validated_data.pop('password')
        user = AppUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
