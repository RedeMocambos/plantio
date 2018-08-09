from rest_framework import serializers
from .models import Especie, Variedade, Interacao, Configuracoes

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

class VariedadeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Variedade
		fields = (
			'nome',
			'descricao',
			'exigencia_solo',
			'tolerancia_poda',
			'exigencia_sol',
			'inicio_colheita',
		)

class InteracaoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Interacao
		fields = (
			'tipo_interacao',
			'especie_a',
			'especie_b',
			'intensidade',
		)	
