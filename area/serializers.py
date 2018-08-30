from rest_framework import serializers
from .models import Area, Localidade

class AreaSerializer(serializers.ModelSerializer):
    localidade = serializers.StringRelatedField(many=False)
    
    class Meta:
        model  = Area
        fields = (
            'id',
            'nome',
            'localidade',
            'dimensao',
            'solo_predominante',
            'microclima',
            'declividade_predominante',
        )


class LocalidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Localidade
        fields = (
            'id',
            'nome',
            'bioma',
            'clima',
        )
