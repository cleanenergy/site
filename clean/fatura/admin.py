# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
<<<<<<< HEAD
from models import Assinatura

admin.site.register(Assinatura)
=======
from fatura.models import Assinatura, Mensalidade
from fatura.forms import AssinaturaAdminForm

class AssinaturaAdmin(admin.ModelAdmin):
	form = AssinaturaAdminForm

admin.site.register(Assinatura, AssinaturaAdmin)
admin.site.register(Mensalidade)
>>>>>>> c359329461fb3c40db454b2cc66cf5873bbbfceb
