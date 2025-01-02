from rest_framework.viewsets import ModelViewSet
from ..models.travel_location import TravelLocation
from ..serializers import TravelLocationSerializer

class TravelLocationViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on TravelLocation.
    """
    queryset = TravelLocation.objects.all()
    serializer_class = TravelLocationSerializer
