from rest_framework.viewsets import ModelViewSet

from .models import Manejo
from .serializers import ManejoSerializer

class ManejoViewSet(ModelViewSet):
    
    queryset = Manejo.objects.all()
    serializer_class = ManejoSerializer

