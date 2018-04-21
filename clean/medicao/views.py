# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, HttpResponse, redirect
from clientes.models import Geradora
from medicao.models import Medida
from medicao.forms import MedidaForm


def medicao_lancar_manual(request):

	if request.POST:
		form = MedidaForm(request.POST)
		if form.is_valid():
			nova_medida =  form.save()
			html = "{ 'status': 'OK', 'save': [{'ug':'" +  nova_medida.ug.id.__str__() + "'}, {'data_hora':'" + nova_medida.data_hora.__str__() + "'}, {'medida':'" + nova_medida.medida.__str__() + "'}] }"
			return HttpResponse(html)
	else:
		form = MedidaForm()

	return render(request, "medicao/lancar.html", {"form" : form})

@csrf_exempt
def medicao_lancar(request):
	if request.POST:
		form = MedidaForm(request.POST)
		if form.is_valid():
			nova_medida =  form.save()
			html = "{ 'status': 'OK', 'save': [{'ug':'" +  nova_medida.ug.id.__str__() + "'}, {'data_hora':'" + nova_medida.data_hora.__str__() + "'}, {'medida':'" + nova_medida.medida.__str__() + "'}] }"
			return HttpResponse(html)
		else:
			html = "{ 'status': 'ERROR', 'info': 'Os seus dados possuem erros. Veja os dados do formulário:<BR>'" + form.as_p()  + "}"
			return HttpResponse(html)

	else:
		return redirect('/medicao/lancar/manual')

