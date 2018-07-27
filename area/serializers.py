from rest_framework import serializers
from .models import Area

class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Area
        fields = (
            'nome',
            'dimensao',
            'solo_predominante',
            'bioma',
            'clima',
            'declividade_predominante',
        )
