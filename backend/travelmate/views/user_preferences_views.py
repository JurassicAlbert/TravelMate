from rest_framework.viewsets import ModelViewSet
from ..models.user_preferences import UserPreferences
from ..serializers import UserPreferencesSerializer


class UserPreferencesViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on UserPreferences.
    """
    queryset = UserPreferences.objects.all()
    serializer_class = UserPreferencesSerializer
