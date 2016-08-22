 #!-*- coding: utf-8 -*-
 
from django.db import models

class Familia(models.Model):
    
    nome  = models.CharField('nome' , max_length=255)
       
