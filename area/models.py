from django.db import models

from especie.models import Configuracoes

class Area(models.Model):

    nome             = models.CharField('nome' , max_length=255, blank=True)
    dimensao         = models.FloatField('dimensao', blank=True)
    solo_predominante = models.TextField('solo predominante', choices=Configuracoes.TIPOS_SOLO, blank=True)
    bioma            = models.TextField('bioma', choices=Configuracoes.TIPOS_BIOMA, blank=True)
    clima            = models.TextField('clima', choices=Configuracoes.TIPOS_CLIMA, blank=True)
    declividade_predominante = models.TextField('declividade predominante', choices=Configuracoes.TIPOS_DECLIVIDADE, blank=True)
