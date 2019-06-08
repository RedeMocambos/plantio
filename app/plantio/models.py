#!-*- coding: utf-8 -*-
import os
from django.db import models

from especie.models import Especie,Configuracoes
from area.models import Area

class Tipos(object):
    UNIDADES_MEDIDA = (
        ('m', 'metro'),
        ('un', 'unidade'),
        ('a', 'area'),
    )

    ESTADOS = (
        ('planejado', 'planejado'),
        ('plantado', 'plantado'),
        ('finalizado/removido', 'finalizado/removido'),
    )
    
    def __init__(self, **kwargs):
        self.unidades_medida = self.prepare_tipo(self.UNIDADES_MEDIDA)
        self.estados = self.prepare_tipo(self.ESTADOS)

    def prepare_tipo(self, values):
        fields = ('valor', 'descricao')
        data = []
        for item in values:
            data.append(dict(zip(fields, item)))
        return data
    
    def get_tipos(self):
        result = {
            'unidades_medida': self.unidades_medida,
            'estados': self.estados,
        }
    

class Plantio(models.Model):
    u""" Classe para definição de plantios """

    UNIDADES_MEDIDA = (
        ('m', 'metro'),
        ('un', 'unidade'),
        ('a', 'area'),
    )

    ESTADOS = (
        ('planejado', 'planejado'),
        ('plantado', 'plantado'),
        ('finalizado/removido', 'finalizado/removido'),
    )
    
    especie          = models.ForeignKey(Especie, on_delete=models.CASCADE, null=True, blank=True)
    area             = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    data_plantio     = models.DateField('data_plantio')
    dimensao         = models.FloatField('dimensao', blank=True)
    unidade_medida   = models.CharField('unidade_medida', choices=Tipos.UNIDADES_MEDIDA, max_length=10)
    espacamento      = models.CharField('espacamento', blank=True, max_length=50)
    densidade        = models.CharField('densidade', blank=True, max_length=50)
    estado           = models.CharField('estado', choices=Tipos.ESTADOS, max_length=20)

    def __str__(self):
        return self.especie.nomes_populares + ' - ' + self.area.nome
