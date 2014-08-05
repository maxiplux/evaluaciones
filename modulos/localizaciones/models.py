# -*- coding: cp1252 -*-
from django.utils import simplejson

from django.db import models
from modulos.maestras.models import Maestra
from modulos.configurador.tuples import MULTIMODO_CHOICES







class RutaMaestra(Maestra):
    class Meta(Maestra.Meta):
        verbose_name = u"Ruta Maestra"
        verbose_name_plural = u"Rutas Maestras"


class Ruta(Maestra):
    maestra= models.ForeignKey(RutaMaestra,related_name="principal")
    multimodo=models.PositiveIntegerField(choices=MULTIMODO_CHOICES,help_text="Como se va utilizar la ruta")
    total_cantidad=models.FloatField(default=0.0,null=True,blank=True)
    total_calidad=models.FloatField(default=0.0,null=True,blank=True)
    notareal=0.0
    @property
    def calificacionreporte(self):
        return self.total_calidad*self.total_cantidad/100

    def __unicode__(self):
        return u'%s/%s nota:%s' % (self.nombre,self.maestra.nombre,self.notareal)
    class Meta(Maestra.Meta):
        verbose_name = u"Ruta"
        #unique_together=('nombre','departamento')
        verbose_name_plural = verbose_name  +"s"




class Departamento(Maestra):
    rutas=models.ManyToManyField(Ruta)
    total_cantidad=models.FloatField(default=0.0,null=True,blank=True)
    total_calidad=models.FloatField(default=0.0,null=True,blank=True)
    @property
    def calificacionreporte(self):
        return self.total_calidad*self.total_cantidad/100
    class Meta(Maestra.Meta):
        verbose_name = u"Departamento"
        verbose_name_plural = verbose_name  +"s"


    def get_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'rutas': [{'id': b.id, 'nombre': b.nombre,'multimodo':b.multimodo,  } for b in self.rutas.all()] }




class Grupo(Maestra):
    departamentos=models.ManyToManyField(Departamento)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    class Meta(Maestra.Meta):
        verbose_name = u"Grupo"
        verbose_name_plural = verbose_name  +"s"
