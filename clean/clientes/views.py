# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def cliente_home(request):
	return render(request, "clientes/clientes_home.html")

