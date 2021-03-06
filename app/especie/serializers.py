from rest_framework import serializers
from .models import Especie, Variedade, Interacao, Configuracoes
from familia.models import Familia

class EspecieSerializer(serializers.ModelSerializer):

    familia = serializers.StringRelatedField(many=False)
    
    class Meta:
        model  = Especie
        fields = (
            'id',
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
            'formas_plantio',
        )

class VariedadeSerializer(serializers.ModelSerializer):
    especie = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Variedade
        fields = (
            'id',
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
            'id',
            'tipo_interacao',
            'familia_a',
            'familia_b',
            'especie_a',
            'especie_b',
            'intensidade',
            'descricao',
        )

class TiposSerializer(serializers.ModelSerializer):
    porte = serializers.SerializerMethodField()
    
    def get_porte(self, obj):
        configuracoes = Configuracoes()
        return configuracoes.get_tipos()['porte']

    class Meta:
        model = None
        fields = (
            'porte',
            'solo',
            'estrato',
            'sucessao',
            'clima',
            'bioma',
            'declividade',
            'fases',
            'unidade_tempo_vida',
            'umidade',
        )
