from rest_framework import serializers
from .models import Especie, Variedade, Interacao, Configuracoes
from familia.models import Familia

class EspecieSerializer(serializers.ModelSerializer):

    familia = serializers.StringRelatedField(many=False)
	
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
			'imagem',
        )

class VariedadeSerializer(serializers.ModelSerializer):
	especie = serializers.StringRelatedField(many=False)
	
	class Meta:
		model = Variedade
		fields = (
			'nome',
			'especie',
			'descricao',
			'exigencia_solo',
			'tolerancia_poda',
			'exigencia_sol',
			'inicio_colheita',
		)

class InteracaoSerializer(serializers.ModelSerializer):
	
	familia_a = serializers.StringRelatedField(many=False)
	familia_b = serializers.StringRelatedField(many=False)
	especie_a = serializers.StringRelatedField(many=False)
	especie_b = serializers.StringRelatedField(many=False)
	
	class Meta:
		model = Interacao
		fields = (
			'tipo_interacao',
			'familia_a',
			'familia_b',
			'especie_a',
			'especie_b',
			'intensidade',
			'descricao',
		)	
