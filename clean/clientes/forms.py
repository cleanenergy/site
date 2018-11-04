# -*- coding: utf-8 -*-

from django import forms
from clientes.models import Cliente

class ClienteEditForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["nome", "logradouro", "bairro", "cidade" , "estado", "cep", "celular"]