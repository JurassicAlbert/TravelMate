from rest_framework.viewsets import ModelViewSet
from ..models.travel_history import TravelHistory
from ..serializers import TravelHistorySerializer


class TravelHistoryViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on TravelHistory.
    """
    queryset = TravelHistory.objects.all()
    serializer_class = TravelHistorySerializer
