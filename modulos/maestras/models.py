# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from modulos.configurador.tuples import *
from modulos.utilidades.util import dcapitalize

# Create your models here.

# Create your models here.
class MaestraBase(models.Model):
    nombre = models.CharField(max_length=255, blank=True)
    creado = models.DateTimeField(auto_now_add=True) # fecha de creacion
    modificado = models.DateTimeField(auto_now=True)# las_modify ultima modificacion
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.nombre)

    @classmethod
    def GetFieldsAdmin(self):
        fields_tmp = self._meta.fields
        fields_tmp = map(lambda x: x.name, fields_tmp)
        return [x for x in fields_tmp if x not in ['id', 'creado', 'modificado','observaciones','comentarios']]




    @classmethod
    def GetFieldsForeignKeyAdmin(self):
        fields_tmp = []

        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsManyToManyKeyAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if type(i) in [models.ManyToManyField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)


    @classmethod
    def GetFieldsForeignKeyResource(self):
        fields_tmp = []
        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name + "__nombre", fields_tmp)

    @classmethod
    def WhoAmI(self):
        return self.__name__

    @classmethod
    def WhoAmIAdmin(self):
        return self.__name__ + "Admin"

    @classmethod
    def GetFieldsSearchAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if type(i) in [models.CharField, models.BigIntegerField, models.PositiveIntegerField, models.EmailField,
                           models.IntegerField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsForeignKeyImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() == "ForeignKey":
                to=field.rel.to
                if to.__bases__[0]==Maestra:
                    fields_tmp.append(field.name)
        return fields_tmp
    @classmethod
    def GetFieldsBooleanImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() in ['BooleanField', "NullBooleanField" ]:
                fields_tmp.append(field.name)
        return fields_tmp


# Create your models here.
class Maestra(models.Model):
    nombre = models.CharField(max_length=255, blank=True, unique=True)
    creado = models.DateTimeField(auto_now_add=True) # fecha de creacion
    modificado = models.DateTimeField(auto_now=True)# las_modify ultima modificacion
    activo = models.BooleanField(default=True, editable=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.nombre)


    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nombre__icontains",)

    @classmethod
    def GetFieldsAdmin(self):
        fields_tmp = self._meta.fields
        fields_tmp = map(lambda x: x.name, fields_tmp)
        return [x for x in fields_tmp if x not in ['id', 'creado', 'modificado','observaciones','comentarios']]

    @classmethod
    def GetFieldsManyToManyKeyAdmin(self):
        fields_tmp = []

        for i,j in self._meta.get_m2m_with_model():

            if type(i) in [models.ManyToManyField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)


    @classmethod
    def GetFieldsForeignKeyAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsForeignKeyResource(self):
        fields_tmp = []
        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name + "__nombre", fields_tmp)

    @classmethod
    def WhoAmI(self):
        return self.__name__

    @classmethod
    def WhoAmIAdmin(self):
        return self.__name__ + "Admin"

    @classmethod
    def GetFieldsSearchAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if type(i) in [models.CharField, models.BigIntegerField, models.PositiveIntegerField, models.EmailField,
                           models.IntegerField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsForeignKeyImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() == "ForeignKey":
                to=field.rel.to
                if to.__bases__[0]==Maestra:
                    fields_tmp.append(field.name)
        return fields_tmp
    @classmethod
    def GetFieldsBooleanImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() in ['BooleanField', "NullBooleanField" ]:
                fields_tmp.append(field.name)
        return fields_tmp



# Create your models here.
class MaestraSimple(models.Model):
    creado = models.DateTimeField(auto_now_add=True) # fecha de creacion
    modificado = models.DateTimeField(auto_now=True)# las_modify ultima modificacion
    activo = models.BooleanField(default=True)



    class Meta:
        abstract = True




    @classmethod
    def GetFieldsAdmin(self):
        fields_tmp = self._meta.fields
        fields_tmp = map(lambda x: x.name, fields_tmp)
        k=[x for x in fields_tmp if x not in ['id', 'creado', 'modificado','observaciones','archivo','comentarios','texto_ejemplo','texto_color','texto','descripcion']]
        k.sort()
        return k


    @classmethod
    def GetFieldsManyToManyKeyAdmin(self):
        fields_tmp = []
        for i in [models.ManyToManyField]:
            if type(i) in [models.ManyToManyField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)


    @classmethod
    def GetFieldsForeignKeyAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsForeignKeyResource(self):
        fields_tmp = []
        for i in self._meta.fields:
            if i.rel and i.name not in ['id', 'creado', 'modificado']:
                fields_tmp.append(i)
        return map(lambda x: x.name + "__nombre", fields_tmp)

    @classmethod
    def WhoAmI(self):
        return self.__name__

    @classmethod
    def WhoAmIAdmin(self):
        return self.__name__ + "Admin"

    @classmethod
    def GetFieldsSearchAdmin(self):
        fields_tmp = []
        for i in self._meta.fields:
            if type(i) in [models.CharField, models.BigIntegerField, models.PositiveIntegerField, models.EmailField,
                           models.IntegerField]:
                fields_tmp.append(i)
        return map(lambda x: x.name, fields_tmp)

    @classmethod
    def GetFieldsForeignKeyImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() == "ForeignKey":
                to=field.rel.to
                if to.__bases__[0]==MaestraSimple:
                    fields_tmp.append(field.name)
        return fields_tmp
    @classmethod
    def GetFieldsBooleanImportExport(self):
        #only for export data with django import and export is a little magic
        fields_tmp = []
        for field in self._meta.fields:
            if field.get_internal_type() in ['BooleanField', "NullBooleanField" ]:
                fields_tmp.append(field.name)
        return fields_tmp



