from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Variedade,Especie,Interacao
from .serializers import EspecieSerializer, VariedadeSerializer, InteracaoSerializer, TiposSerializer
from .metadata import EspecieMetadata

class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
    metadata_class = EspecieMetadata

class VariedadeViewSet(ModelViewSet):
    queryset = Variedade.objects.all()
    serializer_class = VariedadeSerializer


class InteracaoViewSet(ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializer
