from django.contrib import admin

from .models import Especie,Variedade,Fase,Ciclo

admin.site.register(Especie)
admin.site.register(Variedade)
admin.site.register(Ciclo)
admin.site.register(Fase)

