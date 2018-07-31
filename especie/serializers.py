from rest_framework import serializers
from .models import Especie, Variedade, Configuracoes

class EspecieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Especie
        fields = (
            'nome_cientifico',
            'nomes_populares',
            'familia',
            'descricao',
            'temperatura_min',
            'temperatura_max',
            'inicio_colheita',
            'porte',
            'tempo_vida',
            'unidade_tempo_vida',
            'umidade',
            'exigencia_solo',
            'tolerancia_poda',
            'exigencia_solo',
            'inicio_colheita',
            'estrato',
            'sucessao',
            'variedade',
        )