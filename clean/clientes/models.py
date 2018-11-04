# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Cliente(models.Model):
	# Modelo que representa o cliente da empresa. Este possui um usuário sem permissões que dará acesso
	# apenas a interface de monitoramento e acesso de cliente. Seu cadastro principal é localizado pelo 
	# CPF que é o Login para o acesso ao sistema. O Cliente também possui unidades de geração quantas
	# forem contratadas.

	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete = models.SET_NULL,
		related_name="usuario_de",
		null = True,
		blank = True
		)
	id = models.CharField(
		# Identificador do cliente. Este valor pode ser o CPF ou CNPJ do cliente

		max_length=30, 
		primary_key=True,
		help_text="CPF ou CNPJ do cliente",
		verbose_name="CPF/CNPJ",
		)
	nome = models.CharField(
		max_length = 200,
		help_text = "nome do cliente ou razão social",
		verbose_name = "nome ou razão social"
		)
	celular = models.CharField(
		max_length = 20,
		help_text = "telefone celular do cliente",
		verbose_name = "telefone celular"
		)

	# Dados do Endereço de cobrança/contato do cliente. As unidade geradoras do cliente podem
	# ter um endereço diferente desse.
	logradouro = models.CharField(
		max_length = 200,
		help_text = "endereço",
		verbose_name = "endereço",
		blank = False,
		null = False,
		)
	bairro = models.CharField(
		max_length = 150,
		help_text = "bairro",
		verbose_name = "bairro",
		)
	cidade = models.CharField(
		max_length = 150,
		help_text = "cidade",
		verbose_name = "cidade",
		)
	ESTADOS_BRASILEIROS = (
		("AC", "Acre"),
		("AL", "Alagoas"),
		("AP", "Amapá"),
		("AM", "Amazonas"),
		("BA", "Bahia"),
		("CE", "Ceará"),
		("DF", "Distrito Federal"),
		("ES", "Espírito Santo"),
		("GO", "Goiás"),
		("MA", "Maranhão"),
		("MT", "Mato Grosso"),
		("MS", "Mato Grosso do Sul"),
		("MG", "Minas Gerais"),
		("PA", "Pará"),
		("PR", "Paraíba"),
		("PR", "Paraná"),
		("PE", "Pernambuco"),
		("PI", "Piauí"),
		("RJ", "Rio de Janeiro"),
		("RN", "Rio Grande do Norte"),
		("RS", "Rio Grande do Sul"),
		("RO", "Rondônia"),
		("RR", "Roraima"),
		("SC", "Santa Catarina"),
		("SP", "São Paulo"),
		("SE", "Sergipe"),
		("TO", "Tocantins"),
		)
	estado = models.CharField(
		max_length = 2,
		help_text = "estado",
		verbose_name = "estado",
		choices = ESTADOS_BRASILEIROS,
		)
	cep = models.CharField(
		max_length = 9,
		help_text = "CEP(XXXXX-XXX)",
		verbose_name = "CEP da geração",
		)
	# Dados de informação de contato do cliente

	#telefone: 
	class Meta:
		verbose_name = "cliente"
		verbose_name_plural = "clientes"
	def __str__(self):
		return "( " + self.id +" ) - " + self.nome 


class Geradora(models.Model):
	# Modelo que representa uma unidade de geração.

	id = models.AutoField(
		primary_key = True,
		)
	cliente = models.ForeignKey(
		Cliente,
		on_delete = models.CASCADE,
		related_name = "ugs"
		)

	# Endereço onde está instalado a unidade de geração.
	logradouro = models.CharField(
		max_length = 200,
		help_text = "endereço",
		verbose_name = "endereço",
		blank = False,
		null = False,
		)
	bairro = models.CharField(
		max_length = 150,
		help_text = "bairro",
		verbose_name = "bairro",
		)
	cidade = models.CharField(
		max_length = 150,
		help_text = "cidade",
		verbose_name = "cidade",
		)
	ESTADOS_BRASILEIROS = (
		("AC", "Acre"),
		("AL", "Alagoas"),
		("AP", "Amapá"),
		("AM", "Amazonas"),
		("BA", "Bahia"),
		("CE", "Ceará"),
		("DF", "Distrito Federal"),
		("ES", "Espírito Santo"),
		("GO", "Goiás"),
		("MA", "Maranhão"),
		("MT", "Mato Grosso"),
		("MS", "Mato Grosso do Sul"),
		("MG", "Minas Gerais"),
		("PA", "Pará"),
		("PR", "Paraíba"),
		("PR", "Paraná"),
		("PE", "Pernambuco"),
		("PI", "Piauí"),
		("RJ", "Rio de Janeiro"),
		("RN", "Rio Grande do Norte"),
		("RS", "Rio Grande do Sul"),
		("RO", "Rondônia"),
		("RR", "Roraima"),
		("SC", "Santa Catarina"),
		("SP", "São Paulo"),
		("SE", "Sergipe"),
		("TO", "Tocantins"),
		)
	estado = models.CharField(
		max_length = 2,
		help_text = "estado",
		verbose_name = "estado",
		choices = ESTADOS_BRASILEIROS,
		)
	cep = models.CharField(
		max_length = 9,
		help_text = "CEP(XXXXX-XXX)",
		verbose_name = "CEP",
		)
	potencia = models.FloatField(
		help_text = "potência instalada",
		verbose_name = "potência",
		default = 0.640
		)

	class Meta:

		verbose_name = "geradora"
		verbose_name_plural = "geradoras"
		order_with_respect_to = "cliente"

	def __str__(self):
		return  "UG " + self.id.__str__()  + " | ( Cliente: "+ self.cliente.id +" )"

	def code(self):
		return "UG " + self.id.__str__()

	







