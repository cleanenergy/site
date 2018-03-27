# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from clientes.models import Geradora

class Medida(models.Model):
	# Este modelo é responsável por armazenar os dados de medição de uma unidade geradora.
	# Nele será armazenado o valor momentâneo do medidor de campo e a data/hora da medida

	id = models.AutoField(
		primary_key = True
		)
	ug = models.ForeignKey(
		Geradora,
		on_delete = models.CASCADE,
		related_name = "medidas"
		)
	data_hora = models.DateTimeField(
		help_text = "data e hora da medição",
		verbose_name = "data e hora da medição",
		)
	medida = models.PositiveIntegerField(
		help_text = "valor da medição",
		verbose_name = "valor da medição"
		)
	class Meta:
		verbose_name = "medida"
		verbose_name_plural = "medidas"

	def __str__(self):
		return "( UG" + self.ug.id.__str__() + self.ug.cliente.id + " ) - Data/Hora: " + self.data_hora.__str__() + " Valor: " + self.medida.__str__() 

