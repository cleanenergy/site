# -*- coding: utf-8 -*-

from django import forms
from clientes.models import Cliente

class ClienteEditForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["nome", "logradouro", "bairro", "cidade" , "estado", "cep"]
		widgets = {
			"nome": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"logradouro": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"bairro": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"cidade": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"estado": forms.Select( attrs = {
					"class": "form-control",
				}),
			"cep": forms.TextInput( attrs = {
					"class": "form-control",
				}),
		}
		labels = {
			"nome": "Nome Completo",
			"logradouro": "Endereço",
			"bairro": "Bairro",
			"cidade": "Cidade",
			"estado": "Estado",
			"cep": "CEP",
		}