from rest_framework.viewsets import ModelViewSet

from .models import Area, Localidade
from .serializers import AreaSerializer, LocalidadeSerializer

class AreaViewSet(ModelViewSet):
    
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class LocalidadeViewSet(ModelViewSet):
    
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer

