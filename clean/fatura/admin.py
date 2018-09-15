# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fatura.models import Assinatura, Mensalidade
from fatura.forms import AssinaturaAdminForm

class AssinaturaAdmin(admin.ModelAdmin):
	form = AssinaturaAdminForm

admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(Mensalidade)
