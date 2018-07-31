#!-*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import JSONField

from area.models import Area

class PadroesPlantio(models.Model):
    u""" Classe para tipos de padrões de plantio """
    
    descricao        = models.CharField('descricao' , max_length=255, blank=True)
    padrao           = JSONField(null=True, default=[], blank=True)

    def __str__(self):
        return self.descricao

class Manejo(models.Model):
    u""" Classe usada para criar manejos em áreas, a partir de padrões """
    
    descricao        = models.CharField('descricao' , max_length=255, blank=True)
    padrao           = models.ForeignKey(PadroesPlantio, on_delete=models.CASCADE, null=True, blank=True)
    area             = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.descricao
