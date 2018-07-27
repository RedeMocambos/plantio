from rest_framework import serializers
from .models import Fase,Ciclo

class FaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Fase
        fields = (
            'nome',
            'descricao',
            'matriz_porte',
            'floracao',
            'frutificacao',
            'deciduidade',
            'inicio',
            'fim',
            'posicao',
        )


class CicloSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Ciclo
        fields = (
            'nome',
            'fases',
        )
