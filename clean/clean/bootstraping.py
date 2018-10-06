# -*- coding: utf-8 -*-

from django import forms

def Bootstraping(form):

	for field in form.fields:
		if field.errors:
			field.widget.attrs.update({'class': 'form-control is-invalid'})
		else
			field.widget.attrs.update({'class': 'form-control'})
	return form

