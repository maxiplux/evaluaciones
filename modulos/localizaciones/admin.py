# -*- coding: cp1252 -*-
__author__ = 'Juan'
from modulos.utilidades.utiladmin import GenerateAdmins
from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from django.core.exceptions import PermissionDenied

from modulos.localizaciones.models import  *


class CiudadAdmin(ImportExportModelAdmin):
    raw_id_fields = ('deparamento',)

    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'fk': ['deparamento'],

        }

#admin.site.register(Ciudad,CiudadAdmin)
GenerateAdmins([Departamento,Grupo,RutaMaestra,Ruta])
