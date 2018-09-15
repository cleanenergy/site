# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from clientes.models import Cliente
from clientes.models import Geradora

class Assinatura(models.Model):
	
	id = models.AutoField(
		primary_key = True,
		)
	cliente = models.ForeignKey(
		Cliente,
		on_delete = models.CASCADE,
		related_name = "assinaturas"
		)
	ug = models.ForeignKey(
		Geradora,
		on_delete = models.CASCADE,
		related_name = "assinaturas"
		)
	buttonPayPal =  models.URLField(
		blank = True,
		max_length = 500,
		help_text = "link do botão para pagamento",
		verbose_name = "link do botão de pagamento"
		)
	prazo = models.IntegerField(
		blank = False,
		help_text = "prazo de pagamento",
		verbose_name = "prazo",
		)
	valorProjeto = models.DecimalField(
		blank = True,
		help_text = "valor total do projeto",
		verbose_name = "valor do projeto",
		max_digits = 8,
		decimal_places = 2
		)
	valorParticipacao = models.DecimalField(
		blank = True,
		help_text = "valor da participacao da Clean na economia",
		verbose_name = "participação Clean",
		max_digits = 8,
		decimal_places = 2
		)
	valorMensalidade = models.DecimalField(
		blank = True,
		help_text = "valor da mensalidade",
		verbose_name = "mensalidade",
		max_digits = 8,
		decimal_places = 2
		)
	assinado = models.BooleanField(
		default = False,
		help_text = "indica se a assinatura foi assinada pelo cliente",
		verbose_name = "assinada?"
		)
	pendencia = models.BooleanField(
		default = True,
		help_text = "indica se existe alguma pendencia na assinatura",
		verbose_name = "pendências?"
		)
	pagamentoIniciado = models.BooleanField(
		default = False,
		help_text = "indica se houve um início de pagamento da assinatura",
		verbose_name = "iniciou o pagamento?"
		)
	pagamentoConcluido = models.BooleanField(
		default = False,
		help_text = "indica se houve um retorno afirmativo do pagamento da assinatura",
		verbose_name = "tentou pagar?"
		)

	inicio = models.DateField(
		help_text = "data de inicio da assinatura",
		verbose_name = "inicio da assinatura",
		)
	fim = models.DateField(
		help_text = "data de fim da assinatura",
		verbose_name = "fim da assinatura",
		)
	detalhes = models.TextField(
		max_length = 700,
		help_text = "detalhes sobre a fatura",
		verbose_name = "detalhes"
		)

	class Meta:

		verbose_name = "assinatura"
		verbose_name_plural = "assinaturas"
		order_with_respect_to = "inicio"
	
	def __str__(self):
		return "Assinatura: " + str(self.id) + "( Cliente: " + self.cliente.id +" )"