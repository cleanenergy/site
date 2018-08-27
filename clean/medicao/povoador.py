# -*- coding: utf-8 -*-

from medicao.models import Medida
from datetime import datetime, timedelta
from clientes.models import Geradora
import random



def povoar(months_before=6, delta_minutes= 5, power=500, pk_geradora=1, delete_all=False):

	geradora = Geradora.objects.get(pk=pk_geradora)
	hoje = datetime.now()
	medida_inicial = 0
	minutes = timedelta(minutes=delta_minutes)
	step = (power/60)*delta_minutes

	if delete_all:
		Medida.objects.filter(ug=geradora).delete()

	data_inicio = hoje - timedelta(30*months_before)
	data_hora = datetime(data_inicio.year, data_inicio.month, data_inicio.day, 0, 0)
	medida_atual = medida_inicial

	while data_hora < hoje :
		medido = Medida(ug=geradora, data_hora=data_hora, medida=medida_atual)
		medido.save()
		medida_atual = medida_atual + round(getStep(hour=data_hora.hour, minutes = data_hora.minute, max=step), 2)
		data_hora = data_hora + minutes

def getStep(hour, minutes, max):

	if hour < 6:
		return 0
	elif hour < 7:
		if minutes < 10:
			return random.uniform(0, max/100)
		elif minutes < 20:
			return random.uniform(0, max/90)
		elif minutes < 30:
			return random.uniform(0, max/80)
		elif minutes < 40:
			return random.uniform(0, max/70)
		elif minutes < 50:
			return random.uniform(0, max/60)
		else:
			return random.uniform(0, max/50)
	elif hour < 8:
		if minutes < 10:
			return random.uniform(0, max/40)
		elif minutes < 20:
			return random.uniform(0, max/20)
		elif minutes < 30:
			return random.uniform(0, max/10)
		elif minutes < 40:
			return random.uniform(0, max/5)
		elif minutes < 50:
			return random.uniform(0, max/2.5)
		else:
			return random.uniform(0, max/2)
	elif hour < 9:
		if minutes < 10:
			return random.uniform(0, max/1.9)
		elif minutes < 20:
			return random.uniform(0, max/1.8)
		elif minutes < 30:
			return random.uniform(0, max/1.7)
		elif minutes < 40:
			return random.uniform(0, max/1.6)
		elif minutes < 50:
			return random.uniform(0, max/1.5)
		else:
			return random.uniform(0, max/1.4)
	elif hour < 10:
		if minutes < 10:
			return random.uniform(0, max/1.3)
		elif minutes < 20:
			return random.uniform(0, max/1.25)
		elif minutes < 30:
			return random.uniform(0, max/1.20)
		elif minutes < 40:
			return random.uniform(0, max/1.15)
		elif minutes < 50:
			return random.uniform(0, max/1.10)
		else:
			return random.uniform(0, max/1.05)
	elif hour < 15:
		return random.uniform(max/2, max/1)
	elif hour < 16:
		if minutes < 10:
			return random.uniform(0, max/1.01)
		elif minutes < 20:
			return random.uniform(0, max/1.02)
		elif minutes < 30:
			return random.uniform(0, max/1.03)
		elif minutes < 40:
			return random.uniform(0, max/1.04)
		elif minutes < 50:
			return random.uniform(0, max/1.05)
		else:
			return random.uniform(0, max/1.06)
	elif hour < 17:
		if minutes < 10:
			return random.uniform(0, max/1.1)
		elif minutes < 20:
			return random.uniform(0, max/1.15)
		elif minutes < 30:
			return random.uniform(0, max/1.2)
		elif minutes < 40:
			return random.uniform(0, max/1.25)
		elif minutes < 50:
			return random.uniform(0, max/1.30)
		else:
			return random.uniform(0, max/1.35)
	elif hour < 17:
		if minutes < 10:
			return random.uniform(0, max/1.4)
		elif minutes < 20:
			return random.uniform(0, max/1.5)
		elif minutes < 30:
			return random.uniform(0, max/1.6)
		elif minutes < 40:
			return random.uniform(0, max/1.7)
		elif minutes < 50:
			return random.uniform(0, max/1.8)
		else:
			return random.uniform(0, max/1.9)
	elif hour < 18:
		if minutes < 10:
			return random.uniform(0, max/2)
		elif minutes < 20:
			return random.uniform(0, max/4)
		elif minutes < 30:
			return random.uniform(0, max/8)
		elif minutes < 40:
			return random.uniform(0, max/16)
		elif minutes < 50:
			return random.uniform(0, max/32)
		else:
			return random.uniform(0, max/64)
	else:
		return 0

