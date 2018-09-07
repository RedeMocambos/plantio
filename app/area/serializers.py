from rest_framework import serializers
from .models import Area, Localidade

class AreaSerializer(serializers.ModelSerializer):
    localidade = serializers.StringRelatedField(many=False)
    localidade_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model  = Area
        fields = (
            'id',
            'nome',
            'localidade',
            'localidade_id',
            'dimensao',
            'solo_predominante',
            'microclima',
            'declividade_predominante',
            'largura',
            'comprimento',
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
