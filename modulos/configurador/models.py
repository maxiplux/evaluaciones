# -*- coding: cp1252 -*-
from django.db import models
from modulos.maestras.models import Maestra


class Secctor(Maestra):
    class Meta(Maestra.Meta):
        verbose_name = u"Secctor"
        verbose_name_plural = "Secctores empresariales"
