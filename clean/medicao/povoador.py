# -*- coding: utf-8 -*-

from medicao.models import Medida
from datetime import datetime, timedelta
from clientes.models import Geradora
import random



def povoar(meses_antes=2, loops=10, delta_hora= 1, delta_dia=1, limite_random=0.2, pk_geradora=1):

	hoje = datetime.today()
	geradora = Geradora.objects.get(pk=pk_geradora)
	medida_inicial = 0
	d = timedelta(days=delta_dia)
	h = timedelta(hours=delta_hora)

	data_inicio = hoje - timedelta(30*meses_antes)
	data_hora = datetime(data_inicio.year, data_inicio.month, data_inicio.day, 8, 0)
	medida_atual = medida_inicial

	while data_hora.strftime("%Y-%m-%d") != hoje.strftime("%Y-%m-%d"):
		for i in range(0,10):
			medido = Medida(ug=geradora, data_hora=data_hora, medida=medida_atual)
			medido.save()
			medida_atual = medida_atual + round(random.uniform(0,limite_random), 2)
			data_hora = data_hora + h
		data_hora = datetime(data_hora.year, data_hora.month, data_hora.day, 8, 0) + d
