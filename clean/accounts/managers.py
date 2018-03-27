# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

	def create_user(self, username, password=None, **extra_fields):
		'''
		Cria e salva um Usuário com um login dado
		'''
		if not password:
			password = login

		user = self.model(
			username=username,
			**extra_fields
			)
		user.set_password(password)
		user.is_superuser = False
		user.save(using=self._db)
		return user
	def create_superuser(self, username, password, **extra_fields):
		'''
		Cria e salva um superusuário
		'''
		user = self.create_user(
			username = username,
			password = password,
			**extra_fields
			)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user
