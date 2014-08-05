# -*- coding: cp1252 -*-
from django.db import models
from modulos.maestras.models import Maestra


class TipoMenu(Maestra):
    class Meta(Maestra.Meta):
        verbose_name = u"Tipo menu"
        verbose_name_plural = "Tipos de menus"
