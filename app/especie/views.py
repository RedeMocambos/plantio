from rest_framework.viewsets import ModelViewSet

from .models import Variedade,Especie,Interacao,Configuracoes
from .serializers import EspecieSerializer, VariedadeSerializer, InteracaoSerializer

class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer


class VariedadeViewSet(ModelViewSet):
    queryset = Variedade.objects.all()
    serializer_class = VariedadeSerializer


class InteracaoViewSet(ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializer
