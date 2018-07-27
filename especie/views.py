from rest_framework.viewsets import ModelViewSet

from .models import Variedade,Especie,Configuracoes
from .serializers import EspecieSerializer

class EspecieViewSet(ModelViewSet):
    
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

