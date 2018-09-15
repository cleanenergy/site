# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from fatura.models import Assinatura

def fatura_pagar(request):
	assinatura = Assinatura.objects.get(id=1)
	return render(request, 'faturas/fatura_pagar.html', {
		"assinatura": assinatura,
		})
	

def fatura_cancelar(request):

	return HttpResponse("Você cancelou!")

def fatura_processar(request):

	return HttpResponse("Você cancelou!")

def fatura_sucesso(request):

	return HttpResponse("Pagamento processado!")

