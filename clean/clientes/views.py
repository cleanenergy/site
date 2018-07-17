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

		estimativa = 0.0046875			# kWh/Wp		(Estimativa de dados da Clean)
		consumoTV = 0.136				# kWh/h			(TV 55" Sony KD-55X705E)
		consumoCelular = 0.015 			# kWh/carga		(Samsung Galaxy S9)
		consumoMaquinaLavar = 0.27		# kWh/ciclo		(Samsung WD136UVHJWDF)
		consumoLampadaLed = 0.336		# kWh/dia		(Lâmpada 14w equivalente a 100W)
		consumoCarroEletrico = 	0.15	# kWh/km		(Tesla Model S)
		consumoChuveiro = 1.53 			# kWh/minuto	(Chuveiro 5.500W)
		tarifa = 0.83 					# R$/kWh		(Tarifa Cemig bandeira verde 7/2018)


		data = datetime.strptime(request.GET.get("data", datetime.now().strftime("%d-%m-%Y")), "%d-%m-%Y")
		idUg = request.GET.get("ug", None)
		ugs = Geradora.objects.filter(cliente=cliente)

		if idUg:
			ug = Geradora.objects.filter(id=idUg)[:1][0]
			dadosGeracao = getDadosGeracao(ug=ug, cliente=cliente, data=data)

			return render(request, "clientes/clientes_geracao.html", {
				"date": data.strftime("%d-%m-%Y"),
				"ug": ug,
				"ugs": ugs,
				"dadosDia": str(dadosGeracao["dadosDia"]["dados"]),
				"labelsDia": str(dadosGeracao["dadosDia"]["labels"]),
				"dadosMes": str(dadosGeracao["dadosMes"]["dados"]),
				"labelsMes": str(dadosGeracao["dadosMes"]["labels"]),
				"mediaMes": round(dadosGeracao["potenciaInstalada"]*estimativa, 1),
				"dadosAno": str(dadosGeracao["dadosAno"]["dados"]),
				"labelsAno": str(dadosGeracao["dadosAno"]["labels"]),
				"potenciaAtual": round(dadosGeracao["potenciaAtual"], 1),
				"potenciaInstalada": round(dadosGeracao["potenciaInstalada"],0),
				"energiaDia": round(dadosGeracao["energiaDia"], 1),
				"percentualDia": round(dadosGeracao["energiaDia"]/(dadosGeracao["potenciaInstalada"]*estimativa)*100,2),
				"energiaMes": round(dadosGeracao["energiaMes"],1),
				"consumoTV": int(dadosGeracao["energiaMes"]/consumoTV),
				"consumoCelular": int(dadosGeracao["energiaMes"]/consumoCelular),
				"consumoMaquinaLavar": int(dadosGeracao["energiaMes"]/consumoMaquinaLavar),
				"consumoLampadaLed": int(dadosGeracao["energiaMes"]/consumoLampadaLed),
				"consumoCarroEletrico": int(dadosGeracao["energiaMes"]/consumoCarroEletrico),
				"consumoChuveiro": int(dadosGeracao["energiaMes"]/consumoChuveiro),
				"dinheiroMes": round(dadosGeracao["energiaMes"]*tarifa, 2),
				"dinheiroAno": round(dadosGeracao["energiaAno"]*tarifa, 2),
				})
		else:
			ug = ugs.first()
			dadosGeracao = getDadosGeracao(ug=ug, cliente=cliente, data=data)

			return render(request, "clientes/clientes_geracao.html", {
				"date": data.strftime("%d-%m-%Y"),
				"ug": ug,
				"ugs": ugs,
				"dadosDia": str(dadosGeracao["dadosDia"]["dados"]),
				"labelsDia": str(dadosGeracao["dadosDia"]["labels"]),
				"dadosMes": str(dadosGeracao["dadosMes"]["dados"]),
				"labelsMes": str(dadosGeracao["dadosMes"]["labels"]),
				"mediaMes": round(dadosGeracao["potenciaInstalada"]*estimativa, 1),
				"dadosAno": str(dadosGeracao["dadosAno"]["dados"]),
				"labelsAno": str(dadosGeracao["dadosAno"]["labels"]),
				"potenciaAtual": round(dadosGeracao["potenciaAtual"], 1),
				"potenciaInstalada": round(dadosGeracao["potenciaInstalada"],0),
				"energiaDia": round(dadosGeracao["energiaDia"], 1),
				"percentualDia": round(dadosGeracao["energiaDia"]/(dadosGeracao["potenciaInstalada"]*estimativa)*100,2),
				"energiaMes": round(dadosGeracao["energiaMes"],1),
				"consumoTV": int(dadosGeracao["energiaMes"]/consumoTV),
				"consumoCelular": int(dadosGeracao["energiaMes"]/consumoCelular),
				"consumoMaquinaLavar": int(dadosGeracao["energiaMes"]/consumoMaquinaLavar),
				"consumoLampadaLed": int(dadosGeracao["energiaMes"]/consumoLampadaLed),
				"consumoCarroEletrico": int(dadosGeracao["energiaMes"]/consumoCarroEletrico),
				"consumoChuveiro": int(dadosGeracao["energiaMes"]/consumoChuveiro),
				"dinheiroMes": round(dadosGeracao["energiaMes"]*tarifa, 2),
				"dinheiroAno": round(dadosGeracao["energiaAno"]*tarifa, 2),
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


def getDadosGeracao(ug, cliente, data):

	dia = getDadosDia(ug, data)
	mes = getDadosMes(ug, data)
	ano = getDadosAno(ug, data)
	energia = getEnergia(cliente)

	return {
		"dadosDia":{
			"labels": dia["labels"],
			"dados": dia["data"]
		},
		"dadosMes": {
			"labels": mes["labels"],
			"dados": mes["data"],
		},
		"dadosAno":{
			"labels": ano["labels"],
			"dados": ano["data"]
		},
		"potenciaAtual": energia["potenciaAtual"],
		"potenciaInstalada": energia["potenciaInstalada"],
		"energiaDia": energia["energiaDia"],
		"energiaMes": energia["energiaMes"],
		"energiaAno": energia["energiaAno"],


	}

def getDadosDia(ug, data):
	dataInicio = data
	dataFim = data + timedelta(hours=23, minutes=59, seconds=59)

	medidas = Medida.objects.filter(ug=ug, data_hora__gte=dataInicio, data_hora__lte=dataFim).order_by("data_hora")

	labels = list()
	dados = list()

	if medidas.exists():

		anterior = medidas.first()
		medidas = medidas.exclude(id=anterior.id)

		for medida in medidas:
			deltaE = medida.medida - anterior.medida
			deltaT = medida.data_hora - anterior.data_hora
			deltaT = deltaT.total_seconds()/3600
			
			try:
				pot = deltaE/deltaT/1000
			except:
				pot = 0

			dados.append(pot)
			labels.append(medida.data_hora.strftime("%d-%m-%Y %H:%M"))
			anterior = medida
	
	return {
		"labels": labels,
		"data": dados 					#[ kW ]
	}

def getDadosMes(ug, data):
	dataInicio = datetime(data.year, data.month, 1)
	dataFim = datetime(data.year, data.month + 1, 1) - timedelta(seconds=1)

	medidas = Medida.objects.filter(ug=ug, data_hora__gte=dataInicio, data_hora__lte=dataFim).order_by("data_hora")

	labels = list()
	dados = list()

	dia = dataInicio
	d = timedelta(days=1)

	if medidas.exists():

		while(dia <= dataFim):
			inicio = dia
			fim = dia + timedelta(hours=23, minutes=59, seconds=59)
			
			medidasDia = medidas.filter(data_hora__gte=inicio, data_hora__lte=fim).order_by("data_hora")

			try:
				primeiraMedida = medidasDia.first()
				ultimaMedida = medidasDia.last()

				gerado = round(ultimaMedida.medida/1000 - primeiraMedida.medida/1000,2)

			except:
				gerado = 0

			dados.append(gerado)
			labels.append(dia.strftime("%d-%m-%Y"))

			dia = dia + d

	return {
		"labels": labels,
		"data": dados,										# [ kWh ]
	}
def getDadosAno(ug, data):
	dataInicio = datetime(data.year, 1, 1)
	dataFim = datetime(data.year+1, 1, 1) - timedelta(seconds=1)

	medidas = Medida.objects.filter(ug=ug, data_hora__gte=dataInicio, data_hora__lte=dataFim).order_by("data_hora")

	labels = list()
	dados = list()
	mes = 1

	if medidas.exists():

		for m in range(1,13):
			inicio = datetime(data.year, m, 1)
			if m == 12:
				fim = datetime(data.year + 1, 1, 1) - timedelta(seconds=1)
			else:
				fim = datetime(data.year, m + 1, 1) - timedelta(seconds=1)
			
			medidasDia = medidas.filter(data_hora__gte=inicio, data_hora__lte=fim).order_by("data_hora")

			try:
				primeiraMedida = medidasDia.first()
				ultimaMedida = medidasDia.last()

				gerado = round(ultimaMedida.medida/1000 - primeiraMedida.medida/1000,0)
			except:
				gerado = 0

			dados.append(gerado)
			labels.append(inicio.strftime("%m-%Y"))

	return {
		"labels": labels,
		"data": dados 						# [ kWh ]
	}

def getEnergia(cliente):
	ugs = Geradora.objects.filter(cliente = cliente)
	data= datetime.now()

	potenciaInstalada = 0
	potenciaAtual = 0
	energiaDia = 0
	energiaMes = 0
	energiaAno = 0

	for ug in ugs:
		# Dados do dia
		fimDia = datetime(data.year, data.month, data.day, 23, 59, 59)
		inicioDia = datetime(data.year, data.month, data.day)

		medidasDia = Medida.objects.filter(ug=ug, data_hora__gte=inicioDia, data_hora__lte=fimDia).order_by("data_hora")
		print(medidasDia)
		ultimas = Medida.objects.filter(ug=ug).order_by("-data_hora")[:2]
		try:
			deltaE = ultimas[0].medida - ultimas[1].medida
			deltaT = ultimas[0].data_hora - ultimas[1].data_hora
			deltaT = deltaT.total_seconds()/3600
			potenciaAtual = potenciaAtual + (deltaE/deltaT)
		except:
			potenciaAtual = potenciaAtual + 0

		try:
			primeiraMedida = medidasDia.first()
			ultimaMedida = medidasDia.last()
			energiaDia = energiaDia + (ultimaMedida.medida - primeiraMedida.medida)
		except:	
			energiaDia = energiaDia + 0

		# Dados do Mês
		fimMes = datetime(data.year, data.month + 1, 1) - timedelta(seconds=1)
		inicioMes = datetime(data.year, data.month, 1)

		medidasMes = Medida.objects.filter(ug=ug, data_hora__gte=inicioMes, data_hora__lte=fimMes).order_by("data_hora")
		try:
			primeiraMedida = medidasMes.first()
			ultimaMedida = medidasMes.last()
			energiaMes = energiaMes + (ultimaMedida.medida - primeiraMedida.medida)
		except:
			energiaMes = energiaMes + 0

		# Dados do Ano
		fimAno = datetime(data.year + 1, 1, 1) - timedelta(seconds=1)
		inicioAno = datetime(data.year, 1, 1)

		medidasAno = Medida.objects.filter(ug=ug, data_hora__gte=inicioAno, data_hora__lte=fimAno).order_by("data_hora")
		try:
			primeiraMedida = medidasAno.first()
			ultimaMedida = medidasAno.last()
			energiaAno = energiaAno + (ultimaMedida.medida - primeiraMedida.medida)
		except:
			energiaAno = energiaAno + 0

		potenciaInstalada = potenciaInstalada + ug.potencia


	return {
		"potenciaAtual": potenciaAtual,		 			# [ W ]
		"potenciaInstalada": potenciaInstalada*1000,	# [ W ]
		"energiaDia": energiaDia/1000,					# [ kWh ]
		"energiaMes": energiaMes/1000,					# [ kWh ]
		"energiaAno": energiaAno/1000					# [ kWh ]
		}











