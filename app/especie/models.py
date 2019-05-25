#!-*- coding: utf-8 -*-
import os
from django.db import models

from familia.models import Familia


class Configuracoes(object):
    u""" Classe para definição de tipos gerais """
	
    TIPOS_UMIDADE = (
        ('Ultra seco', 'Ultra seco'),
        ('Seco', 'Seco'),
        ('Moderado', 'Moderado'),
        ('Úmido', 'Úmido'),
        ('Ultra úmido', 'Ultra úmido'),
    )
	
    TIPOS_PORTE = (
        ('Aquática', 'Aquática'),
		('Erva pequena', 'Erva pequena'),
        ('Erva média', 'Erva média'),
        ('Erva grande', 'Erva grande'),
        ('Trepadeira', 'Trepadeira'),
        ('Arbusto', 'Arbusto'),
        ('Árvore pequena', 'Árvore pequena'),
        ('Árvore média', 'Árvore média'),
        ('Árvore grande', 'Árvore grande'),
        ('Outro / não especificado', 'Outro / não especificado'),
    )

    TIPOS_SOLO = (
        ('Arenoso', 'Arenoso'),
        ('Areno-siltoso', 'Areno-siltoso'),
        ('Siltoso', 'Siltoso'),
        ('Argiloso', 'Argiloso'),
        ('Argilo-siltoso', 'Argilo-siltoso'),
        ('AE', 'Areno-argiloso'),
        ('Rochoso', 'Rochoso'),
        ('Húmico', 'Húmico'),
        ('Outros', 'Outros')
    )

    NUMBER_RANGE = tuple((n, n) for n in range(10))
	
    TIPOS_ESTRATO = (
        ('Baixo', 'Baixo'),
        ('Médio', 'Médio'),
        ('Alto/dossel', 'Alto/dossel'),
        ('Emergente', 'Emergente'),
	)
	
    TIPOS_SUCESSAO = (
        ('Colonizadora', 'Colonizadora'),
        ('Pioneiras', 'Pioneiras'),
        ('Secundárias iniciais', 'Secundárias iniciais'),
		('Secundárias tardias', 'Secundárias tardias'),
        ('Clímax', 'Clímax'),
	)
	
    TIPOS_CLIMA = (
        ('Tropical úmido', 'Tropical úmido'),
        ('Tropical seco', 'Tropical seco'),
        ('Sub tropical seco', 'Sub tropical seco'),
		('Sub tropical úmido', 'Sub tropical úmido'),
        ('Temperado úmido', 'Temperado úmido'),
        ('Temperado seco', 'Temperado seco')
    )

    TIPOS_BIOMA = (
        ('Cerrado', 'Cerrado'),
        ('Mata atlântica', 'Mata atlântica'),
        ('Floresta estacional semi decidual', 'Floresta estacional semi decidual'),
        ('Pampa', 'Pampa'),
        ('Amazônico', 'Amazônico'),
        ('Pantanal', 'Pantanal')
    )

    TIPOS_DECLIVIDADE = (
        ('Plano', 'Plano'),
        ('Baixada', 'Baixada'),
        ('Encosta acentuada', 'Encosta acentuada'),
        ('Encosta suave', 'Encosta suave')
    )

    FASES = (
        (0, 'Emergência'),
        (1, 'Desenvolvimento juvenil'),
        (2, 'Desenvolvimento pleno'),
        (3, 'Semi-caducidade'),
        (4, 'Caducidade'),
        (-1, 'Poda juvenil'),
        (-2, 'Poda severa'),
    )

    UNIDADE_TEMPO_VIDA = (
        ('D', 'Dias'),
        ('M', 'Meses'),
        ('A', 'Anos')
    )

    fields = (
        'porte',
        'solo',
        'estrato',
        'sucessao',
        'clima',        
        'bioma',
        'declividade',
        'fases',
        'unidade_tempo_vida',
        'umidade',
    )

    def __init__(self, **kwargs):
        self.porte = self.TIPOS_PORTE
        self.solo = self.TIPOS_SOLO
        self.estrato = self.TIPOS_ESTRATO
        self.sucessao = self.TIPOS_SUCESSAO
        self.clima = self.TIPOS_CLIMA
        self.bioma = self.TIPOS_BIOMA
        self.declividade = self.TIPOS_DECLIVIDADE
        self.fases = self.FASES
        self.unidade_tempo_vida = self.UNIDADE_TEMPO_VIDA
        self.umidade = self.TIPOS_UMIDADE


    def get_tipos(self):
        result = {
            'porte': self.TIPOS_PORTE,
            'porte': self.TIPOS_PORTE,
            'solo': self.TIPOS_SOLO,
	        'estrato': self.TIPOS_ESTRATO,
            'sucessao': self.TIPOS_SUCESSAO,
            'clima': self.TIPOS_CLIMA,
            'bioma': self.TIPOS_BIOMA,
            'declividade': self.TIPOS_DECLIVIDADE,
            'fases': self.FASES,
            'unidade_tempo_vida': self.UNIDADE_TEMPO_VIDA,
            'umidade': self.TIPOS_UMIDADE
        }
        return result

    class Meta:
        abstract = True


def get_image_path(instance, filename):
	return os.path.join('images', str(instance.id), filename)

	
class Especie(models.Model):
    u""" Classe para definição de espécies """

    nome_cientifico  = models.CharField('nome_cientifico' , max_length=255, blank=True)
    nomes_populares  = models.CharField('nomes_populares', max_length=1000)
    familia          = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    temperatura_min  = models.IntegerField('temperatura_min', blank=True, null=True)
    temperatura_max  = models.IntegerField('temperatura_max', blank=True, null=True)
    inicio_colheita  = models.IntegerField('inicio_colheita', blank=True, null=True)
    porte            = models.CharField('porte', max_length=30, choices=Configuracoes.TIPOS_PORTE, blank=True)
    tempo_vida       = models.IntegerField('tempo_vida', blank=True, null=True)
    unidade_tempo_vida = models.CharField('unidade_tempo_vida', max_length=1, choices=Configuracoes.UNIDADE_TEMPO_VIDA, default="M")
    umidade          = models.CharField('umidade', max_length=30, choices=Configuracoes.TIPOS_UMIDADE, blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=30, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.PositiveSmallIntegerField('tolerancia_poda', choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.PositiveSmallIntegerField('exigencia_sol', choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    estrato          = models.CharField('estrato', max_length=30, choices=Configuracoes.TIPOS_ESTRATO, blank=True)
    sucessao         = models.CharField('sucessao', max_length=30, choices=Configuracoes.TIPOS_SUCESSAO, blank=True)
    imagem           = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	
    def __str__(self):
        return self.nomes_populares + " (" + self.nome_cientifico + ")"


class Variedade(models.Model):
    u""" Classe para definição de variedades de espécies """
	
    nome             = models.CharField('nome' , max_length=255, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=30, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.PositiveSmallIntegerField('tolerancia_poda', choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.PositiveSmallIntegerField('exigencia_sol', choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, null=True, blank=False)
	
    def __str__(self):
        return self.nome

	
class Interacao(models.Model):
	u"""
	Interação entre especies
	"""

	TIPOS_INTERACAO = (
		('Sinergia', 'Sinergia'),
		('Alelopatia mútua', 'Alelopatia mútua'),
		('Alelopatia própria', 'Alelopatia própria'),
		('Alelopatia alheia', 'Alelopatia alheia'),
	)

	tipo_interacao  = models.CharField('tipo_interacao', max_length=10, choices=TIPOS_INTERACAO, blank=True)
	familia_a       = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='familia_a', null=True, blank=True)
	familia_b       = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='familia_b', null=True, blank=True)
	especie_a       = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='especie_a', null=True, blank=True)
	especie_b       = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='especie_b', null=True, blank=True)
	intensidade     = models.PositiveSmallIntegerField('intensidade', choices=Configuracoes.NUMBER_RANGE, blank=True)
	descricao       = models.TextField('descricao', null=True, blank=True)
	
	def __str__(self):
		
		rotulo = ''
		
		if self.familia_a != None:
		 	rotulo += '(' + self.familia_a.nome + ')'
		if self.familia_a != None and self.familia_b != None:
			rotulo += ' => '
		else:
			rotulo += '_ '		
		if self.familia_b != None:
		 	rotulo += '(' + self.familia_b.nome + ') '
		
		rotulo += self.especie_a.nomes_populares + ' => ' + self.especie_b.nomes_populares + ' ( ' + self.tipo_interacao + ')'

		return rotulo
