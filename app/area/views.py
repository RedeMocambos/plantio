from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Area, Localidade
from .serializers import AreaSerializer, LocalidadeSerializer

class AreaViewSet(ModelViewSet):
    
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class LocalidadeViewSet(ModelViewSet):
    
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer

    @action(methods=['get'], detail=True)
    def areas(self, request, pk=True):
        areas = Area.objects.filter(localidade=pk)
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)
