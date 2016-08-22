 #!-*- coding: utf-8 -*-
from django.db import models
from familia.models import Familia
from tipoPorte.models import TipoPorte

class Especie(models.Model):
    """ """
    
    TIPOS_UMIDADE = (
        ('UC', 'Ultra seco'),
        ('S', 'Seco'),
        ('M', 'Moderado'),
        ('U', 'Úmido'),
        ('UM', 'Ultra úmido'),
    )
    
    nome_cientifico  = models.CharField('nome_cientifico' , max_length=255, blank=True)
    nomes_populares  = models.CharField('nomes_populares', max_length=1000)
    familia          = models.ForeignKey(Familia, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    temperatura_min  = models.IntegerField('temperatura_min', blank=True)
    temperatura_max  = models.IntegerField('temperatura_max', blank=True)    
    inicio_colheita  = models.IntegerField('inicio_colheita', blank=True)
    tempo_vida       = models.IntegerField('tempo_vida', blank=True)
    parceiras        = models.ManyToManyField("self", blank=True)
    antagonistas     = models.ManyToManyField("self", blank=True)
    tipo_porte       = models.ForeignKey(TipoPorte, blank=True)
    altura_porte_min = models.IntegerField('altura_porte_min', blank=True)
    altura_porte_max = models.IntegerField('altura_porte_max', blank=True)
    umidade          = models.CharField('umidade', max_length=2, choices=TIPOS_UMIDADE, blank=True)
    # fotos
        
    def __str__(self):
        return self.titulo.encode('utf8')
