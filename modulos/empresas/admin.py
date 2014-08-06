# -*- coding: cp1252 -*-
from django.contrib import admin
from modulos.empresas.models import Empresas
from modulos.utilidades.utiladmin import GenerateAdmins

GenerateAdmins([Empresas])
# Register your models here.
