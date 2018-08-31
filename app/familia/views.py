from rest_framework.viewsets import ModelViewSet

from .models import Familia
from .serializers import FamiliaSerializer

class FamiliaViewSet(ModelViewSet):
    
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer

