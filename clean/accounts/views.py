# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from accounts.models import User
import hashlib
import datetime
from django.urls import reverse

# Create your views here.

def password_reset_confirm(request):
	if request.method == "POST":
		username = request.POST.get("username", None)
		if username:
			try:
				user = User.objects.get(username = username)
			except:
				return render(request, "accounts/reset_password_confirm.html", {
					"type": 'danger',
					"message": '<strong>Temos um problema!</strong> Este login não está cadastrado em nosso sistema, você está certo deste que este é seu login? Lembre-se que se você é nosso cliente, seu login será seu CPF ou CNPJ.',
					})
			# Cria um código de verificação para ser enviado por e-mail
			code = gen_code(user)

			# Cria um token para validar a mudança que incorpora o código gerado
			token = gen_token(user, code)

			# Obtêm o URL de reset do password
			recovery_link = get_recovery_link(request, token)

			email_hidden = send_recovery_mail(user, recovery_link, code)

			return render(request, "accounts/reset_password_send.html",{
				"email": email_hidden
				})
	if request.method == "GET":
		return render(request, "accounts/reset_password_confirm.html", {
			"type": 'info',
			"message": '<strong>Vamos lá!</strong> Informe seu login e iremos enviar um link para recuperação de senha. Se você é nosso cliente, seu login será seu CPF ou CNPJ.',
			})

def password_reset_confirm_admin(request):
	if request.method == "POST":
		username = request.POST.get("username", None)
		if username:
			try:
				user = User.objects.get(username = username)
			except:
				return render(request, "accounts/reset_password_confirm_admin.html", {
					"type": 'danger',
					"message": '<strong>Temos um problema!</strong> Este login não está cadastrado em nosso sistema, você está certo deste que este é seu login? Lembre-se que se você é nosso cliente, seu login será seu CPF ou CNPJ.',
					})
			# Cria um código de verificação para ser enviado por e-mail
			code = gen_code(user)

			# Cria um token para validar a mudança que incorpora o código gerado
			token = gen_token(user, code)

			# Obtêm o URL de reset do password
			recovery_link = get_recovery_link(request, token)

			email_hidden = send_recovery_mail(user, recovery_link, code)

			return render(request, "accounts/reset_password_send.html",{
				"email": email_hidden
				})
	if request.method == "GET":
		return render(request, "accounts/reset_password_confirm_admin.html", {
			"type": 'info',
			"message": '<strong>Vamos lá!</strong> Informe seu login e iremos enviar um link para recuperação de senha. Se você é nosso cliente, seu login será seu CPF ou CNPJ.',
			})

def password_reset(request, token):
	if request.method == "POST":
		username = request.POST.get("username", None)
		code = request.POST.get("code", None)
		password1 = request.POST.get("password1", None)
		password2 = request.POST.get("password2", "0")
		try:
			user = User.objects.get(username = username)
		except:
			return render(request, "accounts/reset_password_reset.html", {
					'type': 'danger',
					'message': '<strong>Temos um problema! </strong>Este login não está cadastrado em nosso sistema, você está certo deste login? Lembre-se que se você é nosso cliente, seu login será seu CPF ou CNPJ.'
					})
		# Verifica as senhas
		if password1 != password2:
			return render(request, "accounts/reset_password_reset.html", {
					'type': 'danger',
					'message': '<strong>Ops! </strong>As senhas não conferem!'
					})

		# Verifica a validade do token
		if not is_valid_token(user, code, token):
			return render(request, "accounts/reset_password_reset.html", {
					'type': 'danger',
					'message': '<strong>Este link não é mais válido!</strong> Solicite um novo link para redefinir sua senha.'
					})
		user.set_password(password1)
		user.save()
		return render(request, "accounts/reset_password_reset.html",{
			'type': 'success',
			'message': '<strong>Sua senha foi redefinida com sucesso!</strong> Para voltar a tela de login <strong><a href="/login">clique aqui</a></strong>'
			})

	else:
		return render(request, "accounts/reset_password_reset.html",{
			'type': 'info',
			'message': '<strong>Vamos lá!</strong> Por favor, insira os dados para redefinir sua senha.'
			})
def gen_code(user):
	user.date_exp = datetime.date.today() + datetime.timedelta(days=3)
	user.save()
	code = hashlib.md5()
	code.update(user.username + str(datetime.datetime.now()))
	code =  code.hexdigest()[0:6]
	return code

def gen_token(user, code):
	token = hashlib.md5()
	token.update(str(user.date_exp)+str(code)+str(user.username))
	token = token.hexdigest()
	return token

def get_recovery_link(request, token):
	recovery_link = "https://" + request.get_host() + reverse('accounts_password_reset', args=(token,))
	return recovery_link

def is_valid_token(user, code, token):
	token_aux = gen_token(user, code)
	if user.date_exp >= datetime.date.today():
		return token_aux == token
	return False
def send_recovery_mail(user, recovery_link, code):
	send_mail(
		"Recuperação de senha",
		"Recuperação de senha",
		"",
		[user.email],
		fail_silently= False,
		html_message = "<h3>Olá, tudo bem?<br>Você solicitou uma redefinição de senha em nosso site. Acesse <a href="+ recovery_link +">este link</a> para recuperar sua senha.</h3><h1 style='text-align:center;color: red;'>"+ code+"</h3><br><h4 style='text-align:center;'>é seu código de recuperação<br><br><hr><br><p style='text-align:center;'>Muito sol para você!<br>Clean Energy Solutions</p>"
		)
	email_hidden, email_server = str(user.email).split("@")
	email_hidden = email_hidden[0:len(email_hidden)//5] + "********" + email_hidden[len(email_hidden)-len(email_hidden)//5:len(email_hidden)] +"@"
	return email_hidden+email_server
