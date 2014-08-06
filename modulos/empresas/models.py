# -*- coding: cp1252 -*-
from django.db import models

# Create your models here.
from modulos.configurador.tuples import TAMANO_EMPRESA
from modulos.localizaciones.models import Ciudades
from modulos.maestras.models import Maestra
from sorl.thumbnail import ImageField


class Empresas(Maestra):
    ciudad= models.ForeignKey(Ciudades)
    logo= ImageField(upload_to='logos/%d-%m-Y/')
    tamano=models.CharField(max_length=10,choices=TAMANO_EMPRESA(),verbose_name=u"Tamaño")

    def __unicode__(self):
        return u'%s' % (self.nombre)

    class Meta(Maestra.Meta):
        verbose_name = u"Empresa"
        #unique_together=('nombre','departamento')
        verbose_name_plural = verbose_name  +"s"