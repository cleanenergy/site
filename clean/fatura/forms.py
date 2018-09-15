# -*- coding: utf-8 -*-

<<<<<<< HEAD
from django import forms
=======
from django import forms
from fatura.models import Assinatura


class AssinaturaAdminForm(forms.ModelForm):
	class Meta:
		model = Assinatura
		fields = [ 
			"cliente", 
			"ug", 
			"prazo", 
			"valorProjeto", 
			"valorParticipacao", 
			"valorMensalidade", 
			"pagamentoIniciado",
			"pagamentoConcluido",
			"pendencia",
			"urlPagamento",
			"mensalidadesPagas",
			"inicio",
			"pagamentoCartao",
			"detalhes",
			"secret_key",
			]
		widgets = {
			"secret_key": forms.TextInput(attrs={'readonly':'readonly', "style": "width:250px; color:red"}),
		}
>>>>>>> c359329461fb3c40db454b2cc66cf5873bbbfceb
