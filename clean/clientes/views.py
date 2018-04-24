# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from clientes.models import Cliente, Geradora
from clientes.forms import ClienteEditForm
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from medicao.models import Medida
from datetime import timedelta
from accounts.forms import UserChangeFormCliente
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime

@login_required
def cliente_geracao(request):
	try:
		cliente = Cliente.objects.get(user=request.user)
	except ObjectDoesNotExist:
		cliente = None

	if cliente:
		date = datetime.strptime(request.GET.get("date", datetime.now().strftime("%d-%m-%Y")), "%d-%m-%Y")
		idUg = request.GET.get("ug", None)
		periodo = int(request.GET.get("periodo", 2))
		ugs = Geradora.objects.filter(cliente=cliente)

		if idUg:
			ug = Geradora.objects.filter(id=idUg)[:1][0]
			potencia = ug.potencia
			data_inicio = date - timedelta(days=periodo)
			geracao = getGeracao(ug=ug, data_inicio=data_inicio, data_fim=date)

			labels = geracao["labels"]
			dados = geracao["data"]
			energia = geracao["energia"]

			return render(request, "clientes/clientes_geracao.html", {
				"date": date.strftime("%d-%m-%Y"),
				"ug": ug,
				"ugs": ugs,
				"dados": dados,
				"labels": labels,
				"energia": energia,
				"potencia": potencia
				})
		else:
			ug = ugs.first()
			potencia = ug.potencia
			data_inicio = date - timedelta(days=periodo)
			geracao = getGeracao(ug=ug, data_inicio=data_inicio, data_fim=date)

			labels = geracao["labels"]
			dados = geracao["data"]
			energia = geracao["energia"]

			return render(request, "clientes/clientes_geracao.html", {
				"date": date.strftime("%d-%m-%Y"),
				"ug": ug,
				"ugs": ugs,
				"dados": dados,
				"labels": labels,
				"energia": energia,
				"potencia": potencia
				})

	return redirect('/admin/')

@login_required
def cliente_faturas(request):
	try:
		cliente = Cliente.objects.get(user=request.user)
	except ObjectDoesNotExist:
		cliente = None
	if cliente:
		ugs = Geradora.objects.filter(cliente=cliente)
		return render(request, "clientes/clientes_faturas.html", {
			"ugs": ugs
			})
	return redirect('/admin/')

@login_required
def cliente_informacoes_pessoais(request):
	try:
		cliente = Cliente.objects.get(user=request.user)
	except ObjectDoesNotExist:
		cliente = None

	if cliente:
		if request.method == "POST":
			form = ClienteEditForm(request.POST, instance=cliente)
			if form.is_valid():
				form.save()
				return redirect("/clientes/informacoes/")
		else:
			form = ClienteEditForm(instance=cliente)

		return render(request, "clientes/clientes_informacoes.html", {
			"form": form,
			"cliente": cliente,
			"titulo": "Informações Pessoais",
			})
	return redirect('/admin/')

@login_required
def cliente_informacoes_usuario(request):
	try:
		cliente = Cliente.objects.get(user=request.user)
	except ObjectDoesNotExist:
		cliente = None

	if cliente:
		if request.method == "POST":
			form = UserChangeFormCliente(request.POST, instance=cliente.user)
			if form.is_valid():
				form.save()
				return redirect("/clientes/informacoes/")
		else:
			form = UserChangeFormCliente(instance=cliente.user)

		return render(request, "clientes/clientes_informacoes.html", {
			"form": form,
			"cliente": cliente,
			"titulo": "Dados de Usuário",
			})
	return redirect('/admin/')

@login_required
def cliente_informacoes_password(request):
	try:
		cliente = Cliente.objects.get(user=request.user)
	except ObjectDoesNotExist:
		cliente = None
	if cliente:
		if request.method == "POST":
			form = PasswordChangeForm(cliente.user, request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, user)
				return redirect("/clientes/informacoes/")
		else:
			form = PasswordChangeForm(cliente.user)

		return render(request, "clientes/clientes_informacoes.html", {
			"form": form,
			"cliente": cliente,
			"titulo": "Mudar Senha",
			})
	return redirect('/admin/')


def getGeracao(ug, data_inicio, data_fim):
"""
	medidas = Medida.objects.filter(ug=ug, data_hora__gt=data_inicio, data_hora__lt=data_fim)
	try: 
		anterior = medidas[0]
	except:
		anterior = None
	energia = 0
	labels = list()
	data = list()
	if anterior:
		medidas.order_by("data_hora")
		anterior = medidas.first()
		medidas = medidas.exclude(id = anterior.id)
		for medida in medidas:
			delta = medida.medida - anterior.medida
			data.append(delta)
			labels.append(anterior.data_hora.strftime("%d-%m-%Y %H:%M"))
			energia = energia + delta
			anterior = medida
"""
	return {
		"energia": 0,
		"data": [],
		"labels": []
	}










