from rest_framework import serializers
from .models import Manejo,PadroesPlantio

class ManejoSerializer(serializers.ModelSerializer):

    padrao = serializers.SlugRelatedField(many=False, slug_field='padrao', read_only=True)
    
    class Meta:
        model  = Manejo
        fields = (
            'descricao',
            'padrao',
        )
