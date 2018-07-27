from rest_framework.viewsets import ModelViewSet

from .models import Area
from .serializers import AreaSerializer

class AreaViewSet(ModelViewSet):
    
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

