from django.db import models

from especie.models import Configuracoes

class Localidade(models.Model):
    u""" Localidade """

    nome = models.CharField('nome' , max_length=255, blank=True)
    bioma = models.CharField('bioma', max_length=255, choices=Configuracoes.TIPOS_BIOMA, blank=True)
    clima = models.CharField('clima', max_length=255, choices=Configuracoes.TIPOS_CLIMA, blank=True)
    cidade = models.CharField('cidade', max_length=255, blank=True)
    
    def __str__(self):
        return self.nome

	
class Area(models.Model):
    u""" Classe para definição de áreas """

    nome = models.CharField('nome' , max_length=255, blank=True)
    dimensao = models.FloatField('dimensao', blank=True)
    largura = models.FloatField('largura', blank=True, default=0)
    comprimento = models.FloatField('comprimento', blank=True, default=0)
    solo_predominante = models.TextField('solo predominante', choices=Configuracoes.TIPOS_SOLO, blank=True)
    declividade_predominante = models.TextField('declividade predominante', choices=Configuracoes.TIPOS_DECLIVIDADE, blank=True)
    localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, null=True, blank=False)
    microclima = models.TextField('microclima', choices=Configuracoes.MICROCLIMAS, null=True, blank=True)
    
    def __str__(self):
        return self.nome + ' (' + self.localidade.nome + ')'
