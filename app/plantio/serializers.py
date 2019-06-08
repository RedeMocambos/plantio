from rest_framework import serializers
from .models import Plantio
from especie.models import Especie
from area.models import Area

class PlantioSerializer(serializers.ModelSerializer):
    
    especie = serializers.StringRelatedField(many=False)
    area = serializers.StringRelatedField(many=False)
    
    class Meta:
        model  = Plantio
        fields = (
            'id',
            'especie',
            'area',
            'data_plantio',
            'dimensao',
            'unidade_medida',
            'espacamento',
            'densidade',
            'estado',
        )
