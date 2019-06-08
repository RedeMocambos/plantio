from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Plantio
from .serializers import PlantioSerializer
from .metadata import PlantioMetadata

class PlantioViewSet(ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer
    metadata_class = PlantioMetadata
