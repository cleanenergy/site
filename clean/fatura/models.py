# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib

from django.db import models
from clientes.models import Cliente
from clientes.models import Geradora

class Assinatura(models.Model):
	
	id = models.AutoField(
		primary_key = True,
		)
	secret_key = models.CharField(
		default = "A chave secreta será gerada automaticamente",
		max_length = 700,
		help_text = "chave secreta para confirmação de pagamentos",
		verbose_name = "chave secreta",
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
	prazo = models.IntegerField(
		blank = False,
		help_text = "prazo de pagamento em meses",
		verbose_name = "prazo",
		)
	valorProjeto = models.DecimalField(
		default = 5700,
		help_text = "valor total do projeto",
		verbose_name = "valor do projeto",
		max_digits = 10,
		decimal_places = 2
		)
	valorParticipacao = models.DecimalField(
		default = 60,
		help_text = "valor da participacao da Clean na economia",
		verbose_name = "participação Clean",
		max_digits = 8,
		decimal_places = 2
		)
	valorMensalidade = models.DecimalField(
		default = 297.5,
		help_text = "valor da mensalidade",
		verbose_name = "mensalidade",
		max_digits = 8,
		decimal_places = 2
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
	pendencia = models.BooleanField(
		default = True,
		help_text = "indica se há alguma pendência no pagamento.",
		verbose_name = "existe pendencias de pagamento?"
		)
	urlPagamento = models.URLField(
		blank = True,
		help_text = "URL para assinar mensalidades de forma recorrente no cartão de crédito",
		verbose_name = "URL da assinatura",
		max_length = 700,
		)
	mensalidadesPagas = models.IntegerField(
		default = 0,
		help_text = "indica o numero de parcelas pagas pelo cliente",
		verbose_name = "parcelas pagas"
		)
	inicio = models.DateField(
		help_text = "data de inicio da assinatura",
		verbose_name = "inicio da assinatura",
		)
	pagamentoCartao = models.BooleanField(
		default = True,
		help_text = "indica a opção de pagamento do cliente",
		verbose_name = "forma de pagamento",
		choices = (
			(True, "Cartão de Crédito"),
			(False, "Boleto Bancário"),
			)
		)
	detalhes = models.TextField(
		blank = True,
		max_length = 700,
		help_text = "detalhes sobre pendência na assinatura",
		verbose_name = "detalhes de pendencia"
		)

	class Meta:

		verbose_name = "assinatura"
		verbose_name_plural = "assinaturas"
		order_with_respect_to = "cliente"
	
	def __str__(self):
		return "Assinatura: " + str(self.id) + " | ( Cliente: " + self.cliente.id +" )"

	def save(self, *args, **kwargs):
		k = hashlib.md5()
		k.update(self.cliente.id + str(self.ug.id) + str(self.id))
		self.secret_key =  k.hexdigest()
		super(Assinatura, self).save(*args, **kwargs)

class Mensalidade(models.Model):

	id = models.AutoField(
		primary_key = True,
		)
	assinatura = models.ForeignKey(
		Assinatura,
		on_delete = models.CASCADE,
		related_name = "mensalidades",
		)
	vencimento = models.DateField(
		help_text = "data de vencimento da mensalidade",
		verbose_name = "vencimento",
		)
	valor = models.DecimalField(
		default = 297.5,
		help_text = "valor da mensalidade",
		verbose_name = "valor",
		max_digits = 8,
		decimal_places = 2,
		)
	pago = models.BooleanField(
		help_text = "mensalidade foi paga?",
		verbose_name = "pago?",
		)
	urlPagamento = models.URLField(
		help_text = "URL para pagamento da mensalidade",
		verbose_name = "URL de pagamento",
		max_length = 700,
		)
	nParcela = models.IntegerField(
		help_text = "mês de referência da parcela",
		verbose_name = "número da parcela",
		)
	class Meta:

		verbose_name = "mensalidade"
		verbose_name_plural = "mensalidades"
		order_with_respect_to = "assinatura"
	
	def __str__(self):
		return "Assinatura: " + str(self.assinatura.id) + " | ( Mensalidade: " + str(self.nParcela) + " / " + str(self.assinatura.prazo) + " )"
