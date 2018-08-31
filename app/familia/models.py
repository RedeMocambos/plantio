#!-*- coding: utf-8 -*-
 
from django.db import models

class Familia(models.Model):
    u""" Classe para descrever famílias botânicas """
    
    nome = models.CharField('nome' , max_length=255)
       

    def __str__(self):
        return self.nome
