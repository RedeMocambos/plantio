from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Variedade,Especie,Interacao
from .serializers import EspecieSerializer, VariedadeSerializer, InteracaoSerializer, TiposSerializer
from .metadata import EspecieMetadata

class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
    metadata_class = EspecieMetadata

class VariedadeViewSet(ModelViewSet):
    queryset = Variedade.objects.all()
    serializer_class = VariedadeSerializer


class InteracaoViewSet(ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializer

"""
class TiposViewSet(ModelViewSet):
    configuracoes = Configuracoes()
    
    queryset = configuracoes.get_tipos()
    serializer_class = TiposSerializer
    
    def list(self, request):
        configuracoes = Configuracoes()
        
        serializer = TiposSerializer(
            instance = configuracoes.get_tipos(),
            many=True
        )
        print('------------')
        print(serializer.data)
        return Response(serializer.data)
    

    tipos = configuracoes.get_tipos()
    porte = tipos['porte']
    solo = tipos['solo']
    estrato = tipos['estrato']
    sucessao = tipos['sucessao']
    clima = tipos['clima']
    bioma = tipos['bioma']
    declividade = tipos['declividade']
    fases = tipos['fases']
    unidade_tempo_vida = tipos['unidade_tempo_vida']
    umidade = tipos['umidade']
    """

