from rest_framework.metadata import SimpleMetadata

from .models import Configuracoes

class EspecieMetadata(SimpleMetadata):

    def get_choices(self):
        configuracoes = Configuracoes()
        
        return configuracoes.get_tipos()

    def determine_metadata(self, request, view):
        return {
            'choices': self.get_choices()
        }
