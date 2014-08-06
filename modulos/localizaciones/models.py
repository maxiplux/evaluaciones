# -*- coding: cp1252 -*-
from django.utils import simplejson

from django.db import models
from modulos.maestras.models import Maestra
from modulos.configurador.tuples import MULTIMODO_CHOICES







class Paises(Maestra):

    def __unicode__(self):
        return u'%s/%s nota:%s' % (self.nombre)
    class Meta(Maestra.Meta):
        verbose_name = u"Pais"
        #unique_together=('nombre','departamento')
        verbose_name_plural = verbose_name  +"ses"


class Departamentos(Maestra):
    pais= models.ForeignKey(Paises)
    def __unicode__(self):
        return u'%s/%s ' % (self.pais.nombre,self.nombre)

    class Meta(Maestra.Meta):
        verbose_name = u"Departamento"
        verbose_name_plural = verbose_name + "s"

class Ciudades(Maestra):
    departamento= models.ForeignKey(Departamentos)
    def __unicode__(self):
        return u'%s/%s ' % (self.departamento.nombre,self.nombre)

    class Meta(Maestra.Meta):
        verbose_name = u"Ciudad"
        verbose_name_plural = verbose_name + "ses"