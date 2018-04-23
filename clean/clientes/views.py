# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def cliente_geracao(request):
	return render(request, "clientes/clientes_geracao.html")

