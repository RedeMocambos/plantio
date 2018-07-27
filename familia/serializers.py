from rest_framework import serializers
from .models import Familia

class FamiliaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Familia
        fields = (
            'nome',
        )
