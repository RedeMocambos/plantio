 #!-*- coding: utf-8 -*-
 
from django.db import models

class TipoPorte(models.Model):
    """ """

    # nome - erva, arbusto, árvore pequena, árvore grande, trepadeira,
    # área - m2 ?
    
    porte  = models.CharField('porte' , max_length=255)
    area = models.IntegerField('area', blank=True)
