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
		data = request.GET.get("data", None)
		idUg = request.GET.get("ug", None)
		ugs = Geradora.objects.filter(cliente=cliente)

		if data and idUg:
			ug = Geradora.objects.filter(id=idUg)[:1][0]
			data_inicio = datetime.now() - timedelta(days=float(data))
			geracao = getGeracao(ug=ug)

			labels = geracao["labels"]
			dados = geracao["data"]
			energia = geracao["energia"]

			return render(request, "clientes/clientes_geracao.html", {
				"data": data,
				"ug": ug.pk,
				"ugs": ugs,
				"dados": dados,
				"labels": labels,
				"energia": energia
				})
		else:
			data = 1
			ug = ugs[0]
			data_inicio = datetime.now() - timedelta(days=float(data))
			geracao = getGeracao(ug=ug)

			labels = geracao["labels"]
			dados = geracao["data"]
			energia = geracao["energia"]

			return render(request, "clientes/clientes_geracao.html", {
				"data": data,
				"ug": ug.pk,
				"ugs": ugs,
				"dados": dados,
				"labels": labels,
				"energia": energia
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


def getGeracao(ug):
	medidas = Medida.objects.all().order_by("data_hora")
	energia = 0
	labels = list()
	data = list()
	anterior = medidas[0]
	medidas = medidas.exclude(id = anterior.id)

	for medida in medidas:
		delta = medida.medida - anterior.medida
		data.append(delta)
		labels.append(anterior.data_hora.strftime("%d-%m-%Y %H:%M"))
		energia = energia + delta
		anterior = medida
	return {
		"energia": energia,
		"data": data,
		"labels": labels
	}










