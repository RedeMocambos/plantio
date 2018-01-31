 #!-*- coding: utf-8 -*-
from django.db import models
from familia.models import Familia
#from tipoPorte.models import TipoPorte

class Configuracoes():
        TIPOS_UMIDADE = (
            ('UC', 'Ultra seco'),
            ('S', 'Seco'),
            ('M', 'Moderado'),
            ('U', 'Úmido'),
            ('UM', 'Ultra úmido'),
        )
        
        TIPOS_PORTE = (
            ('AQ', 'Aquática'),
            ('EP', 'Erva pequena'),
            ('EM', 'Erva média'),
            ('EG', 'Erva grande'),
            ('TP', 'Trepadeira'),
            ('AB', 'Arbusto'),
            ('AP', 'Árvore pequena'),
            ('AM', 'Árvore média'),
            ('AG', 'Árvore grande'),
            ('NA', 'Outro / não especificado'),
        )
        
        TIPOS_SOLO = (
            ('AE', 'Arenoso'),
            ('AE', 'Areno-siltoso'),
            ('SL', 'Siltoso'),
            ('AG', 'Argiloso'),
            ('AS', 'Argilo-siltoso'),        
            ('AE', 'Areno-argiloso'),
            ('RC', 'Rochoso'),
            ('HU', 'Húmico'),
        )
        
        NUMBER_RANGE = (
            ('0', '0'), 
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
        )
        
        TIPOS_ESTRATO = (
            ('B', 'Baixo'),
            ('M', 'Médio'),
            ('A', 'Alto/dossel'),
            ('E', 'Emergente'),
        )
        
        TIPOS_SUCESSAO = (
            ('CO', 'Colonizadora'),
            ('PI', 'Pioneiras'),
            ('SI', 'Secundárias iniciais'),
            ('ST', 'Secundárias tardias'),
            ('CL', 'Clímax'),
        )

        
class Variedade(models.Model):

    nome             = models.CharField('nome' , max_length=255, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=2, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.CharField('tolerancia_poda', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.CharField('exigencia_sol', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    
    def __str__(self):
        return self.nome


class Especie(models.Model):
    """ """
    
    nome_cientifico  = models.CharField('nome_cientifico' , max_length=255, blank=True)
    nomes_populares  = models.CharField('nomes_populares', max_length=1000)
    familia          = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    temperatura_min  = models.IntegerField('temperatura_min', blank=True, null=True)
    temperatura_max  = models.IntegerField('temperatura_max', blank=True, null=True)
    inicio_colheita  = models.IntegerField('inicio_colheita', blank=True, null=True)
    porte            = models.CharField('porte', max_length=2, choices=Configuracoes.TIPOS_PORTE, blank=True)
    #tempo_vida       = models.IntegerField('tempo_vida', blank=True)
    #parceiras        = models.ManyToManyField("self", blank=True)
    #antagonistas     = models.ManyToManyField("self", blank=True)
    umidade          = models.CharField('umidade', max_length=2, choices=Configuracoes.TIPOS_UMIDADE, blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=2, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.CharField('tolerancia_poda', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.CharField('exigencia_sol', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    estrato          = models.CharField('estrato', max_length=2, choices=Configuracoes.TIPOS_ESTRATO, blank=True)
    sucessao         = models.CharField('sucessao', max_length=2, choices=Configuracoes.TIPOS_SUCESSAO, blank=True)
    variedade        = models.ForeignKey('variedade', on_delete=models.CASCADE, related_name='Variedade', null=True, blank=True)
    
    # fotos
        
    def __str__(self):
        return self.nomes_populares + " (" + self.nome_cientifico + ")"


