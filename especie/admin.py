from django.contrib import admin

from .models import Especie,Variedade,Interacao

admin.site.register(Especie)
admin.site.register(Variedade)
admin.site.register(Interacao)
