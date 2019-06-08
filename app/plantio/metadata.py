from rest_framework.metadata import SimpleMetadata

from .models import Tipos

class PlantioMetadata(SimpleMetadata):

    def get_choices(self):
        tipos = Tipos()
        
        return tipos.get_tipos()

    def determine_metadata(self, request, view):
        return {
            'choices': self.get_choices()
        }
