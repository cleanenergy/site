# -*- coding: utf-8 -*-

from django import forms
from medicao.models import Medida

class MedidaForm(forms.ModelForm):

	data_hora = forms.DateTimeField(
		widget= forms.DateTimeInput( format="%Y-%m-%dT%H:%M%" ,attrs = {
				'class': 'form-control',
				'type': 'datetime-local',
			}),
		input_formats = [
			'%Y-%m-%dT%H:%M',
			'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
			'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
			'%Y-%m-%d',             # '2006-10-25'
			'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
			'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
			'%m/%d/%Y',             # '10/25/2006'
			'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
			'%m/%d/%y %H:%M',       # '10/25/06 14:30'
			'%m/%d/%y'             # '10/25/06'
			]
		)

	class Meta:
		model = Medida
		fields = ["ug","data_hora", "medida"]
		widgets = {
			'ug': forms.Select( attrs = {
					'class': 'form-control',
				}),
			'medida': forms.NumberInput( attrs = {
					'class': 'form-control',
				})
		}
