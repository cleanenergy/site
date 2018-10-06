# -*- coding: utf-8 -*-

from django import forms
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(
		label = "senha",
		widget = forms.PasswordInput,
		)
	password2 = forms.CharField(
		label = "confirmação",
		widget = forms.PasswordInput,
		)

	class Meta:
		model = User
		fields = ("nome", "sobrenome", "email")

	def clean_password2(self):
		# Checa se as senhas são iguais
		password1 = self.cleaned_data.get("password1")
		password2 = self. cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidatioError("As senhas não conferem")
		return password2

	def save(self, commit=True):
		# Salva o usuário
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
# Formulário para alteração de Usuário
	password = ReadOnlyPasswordHashField()
	username = forms.CharField(
			label = "Login",
			disabled = True,
			)

	class Meta:
		model = User
		fields = (
			"nome",
			"sobrenome",
			"username",
			"email",
			"is_staff",
			"is_superuser",
			)
	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]

class UserChangeFormCliente(forms.ModelForm):
# Formulário para alteração de Usuário

	class Meta:
		model = User
		fields = (
			"nome",
			"sobrenome",
			"email",
			)
		widgets = {
			"nome": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"sobrenome": forms.TextInput( attrs = {
					"class": "form-control",
				}),
			"email": forms.EmailInput( attrs = {
					"class": "form-control",
				}),
		}
		labels = {
			"nome": "Nome",
			"sobrenome": "Sobrenome",
			"email": "Email",
		}

class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserChangeForm
	add_form = UserCreationForm

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('nome','sobrenome','email', 'is_staff')
	list_filter = ('is_staff',)
	fieldsets = (
		("Login", {'fields': ('username', 'email', 'password')}),
		('Informações Pessoais', {'fields': ("nome","sobrenome")}),
		('Permissões', {'fields': ('is_staff','is_superuser')}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user
	add_fieldsets = (
    	(None, {
    		'classes': ('wide',),
    		'fields': ('nome', 'sobrenome', 'email', 'username', 'password1', 'password2')}
    	),
	)
	search_fields = ('nome','sobrenome',)
	ordering = ('nome','sobrenome',)
	filter_horizontal = ()

