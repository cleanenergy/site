# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from fatura.models import Assinatura

def fatura_sucesso(request, assinaturaId = None):
	if assinaturaId :
		try:
			assinatura = Assinatura.objects.get(id=assinaturaId)
		except ObjectDoesNotExist:
			assinatura = None

		if assinatura :
			if assinatura.secret_key == request.GET.get("key", None): 
				assinatura.pagamentoIniciado = True
				assinatura.pendencia = True
				assinatura.detalhes = "Não se preocupe, seu pagamento já foi cadastrado, falta apenas confirmar o débito junto a operadora do cartão. Qualquer problema entraremos em contato."
				assinatura.save()

				return render(request, "faturas/fatura_sucesso.html",{
					"next": reverse("cliente_financeiro"),
					})
			else:
				return render(request, "faturas/fatura_erro.html",{
					"next": reverse("cliente_financeiro"),
					})

	redirect("cliente_financeiro")

def fatura_pagar(request, assinaturaId = None):
	if assinaturaId :
		try:
			assinatura = Assinatura.objects.get(id=assinaturaId)
		except ObjectDoesNotExist:
			assinatura = None

		if assinatura :
			return render(request, "faturas/fatura_pagar.html",{
				"next": assinatura.urlPagamento,
				})
	redirect("cliente_financeiro")

	

