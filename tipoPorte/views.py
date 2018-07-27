from rest_framework.viewsets import ModelViewSet

from .models import Fase,Ciclo
from .serializers import FaseSerializer,CicloSerializer

class FaseViewSet(ModelViewSet):
    
    queryset = Fase.objects.all()
    serializer_class = FaseSerializer

class CicloViewSet(ModelViewSet):
    
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer
