from rest_framework.viewsets import ModelViewSet

from .models import PadroesPlantio,Manejo
from .serializers import ManejoSerializer,PadroesPlantioSerializer

class ManejoViewSet(ModelViewSet):
    
    queryset = Manejo.objects.all()
    serializer_class = ManejoSerializer


class PadroesPlantioViewSet(ModelViewSet):
    
    queryset = PadroesPlantio.objects.all()
    serializer_class = PadroesPlantioSerializer

