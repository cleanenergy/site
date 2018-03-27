# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
	 
	username = models.CharField(
		# O usuário dos clientes será composto pelo CPF ou CNPJ do cliente. Mas por questões de administração, 
		# não iremos limitar o username, para criarmos logins de superusuários e administrativos por questões de gestão

		max_length=30, 
		primary_key=True,
		help_text="insira seu CPF",
		verbose_name="login",
		)
	nome = models.CharField(
		max_length=100, 
		help_text="nome do usuário",
		verbose_name="nome",
		)
	sobrenome = models.CharField(
		max_length=200, 
		help_text="sobrenome do usuário",
		verbose_name="sobrenome",
		)
	email = models.EmailField(
		max_length=200,
		null=True,
		blank=True,
		help_text="endereço de e-mail do usuário",
		verbose_name="email",
		)
	is_active = models.BooleanField(
		verbose_name="ativo",
		default = True,
		)
	is_staff = models.BooleanField(
		verbose_name="staff",
		default = False,
		)

	objects = UserManager()

	class Meta:
		verbose_name = "usuário"
		verbose_name_plural = "usuários"
		permissions = (
			("funcionario", "Acesso às ferramentas de controle e gestão do sistema"),
			("cliente", "Acesso restrito a área de cliente"),
			)

	def get_full_name(self):
		return self.nome + " " + self.sobrenome

	def get_short_name(self):
		return self.nome

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'
