from django.db import models

from especie.models import Configuracoes

class Localidade(models.Model):
    u""" Localidade """

    nome = models.CharField('nome' , max_length=255, blank=True)
    bioma = models.CharField('bioma', max_length=255, choices=Configuracoes.TIPOS_BIOMA, blank=True)
    clima = models.CharField('clima', max_length=255, choices=Configuracoes.TIPOS_CLIMA, blank=True)

    def __str__(self):
        return self.nome

	
class Area(models.Model):
    u""" Classe para definição de áreas """

    MICROCLIMAS =  (
        ('Campo aberto', 'Campo aberto'),
        ('Capoeira rala', 'Capoeira rala'),
        ('Capoeira densa', 'Capoeira densa'),
        ('Mata fechada', 'Mata fechada'),
        ('Chapada', 'Chapada'),
        ('Grota', 'Grota'),
        ('Baixada', 'Baixada'),
        ('Topo de morro', 'Topo de morro'),
    )
    
    nome = models.CharField('nome' , max_length=255, blank=True)
    dimensao = models.FloatField('dimensao', blank=True)
    solo_predominante = models.TextField('solo predominante', choices=Configuracoes.TIPOS_SOLO, blank=True)
    declividade_predominante = models.TextField('declividade predominante', choices=Configuracoes.TIPOS_DECLIVIDADE, blank=True)
    localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, null=True, blank=False)
    microclima = models.TextField('microclima', choices=MICROCLIMAS, null=True, blank=True)
    
    def __str__(self):
        return self.nome
