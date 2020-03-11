from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Familia(models.Model):
    nome_popular = models.CharField(_('Nome Popular'), max_length=80)
    nome_cientifico = models.CharField(_('Nome Científico'), max_length=80)     
    descricao = models.TextField(null=True, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='familias/')
    referencia = models.CharField(_('Referência'), max_length=80, null=True)

    def __str__(self):
        return self.nome_popular

class Arvore(models.Model):
    nome_popular = models.CharField(_('Nome Popular'), max_length=80)
    nome_cientifico = models.CharField(_('Nome Científico'), max_length=80)
    descricao = models.TextField(null=True, verbose_name='Descrição')
    referencia = models.CharField(_('Referência'), max_length=80, null=True) 
    familia =  models.ForeignKey(Familia, models.PROTECT, null=False)
    imagem = models.ImageField(upload_to='arvores/')

    def __str__(self):
        return self.nome_popular