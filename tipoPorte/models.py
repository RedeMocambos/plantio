 #!-*- coding: utf-8 -*-
from django.db import models

from django.contrib.postgres.fields import JSONField
from especie.models import Especie


class Fase(models.Model):
    nome             = models.CharField('nome' , max_length=255, blank=True)   
    descricao        = models.TextField('descricao', blank=True)
    matriz_porte     = JSONField(null=True, default=[], blank=True)
    floracao         = models.BooleanField('floracao', default=False)
    frutificacao     = models.BooleanField('frutificacao', default=False)
    deciduidade      = models.BooleanField('deciduidade', default=False)
    inicio           = models.CharField('inicio_fase', max_length=5, blank=True)
    fim              = models.CharField('fim_fase', max_length=5, blank=True)
    #    ciclo            = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='Ciclo')
    
    def __str__(self):
        if self.nome != '':
            return self.nome
        else:
            return '(nome vazio)'        
    

class Ciclo(models.Model):
    nome             = models.CharField('nome' , max_length=255, blank=True)
    fases            = models.ManyToManyField(Fase, related_name='Fase', default=False)
    especie          = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='Especie')
    
    def __str__(self):
        return self.nome + "(" + self.especie.nome_cientifico + ")"
    

class TipoPorte(models.Model):
    nome             = models.CharField('nome' , max_length=255, blank=True)

    def __str__(self):
        return self.nome


#    porte
    
'''
    nome      not null
    ordem     smallint not null
* descricao
* matrizPorte   json
* floracao      bool
* frutificacao  bool
* deciduidade   bool ? dúvida: seria necessário um descritor específico ?
'''
