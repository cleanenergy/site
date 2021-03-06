"""clean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from clientes import views

urlpatterns = [
	url(r'^geracao/$', views.cliente_geracao, name="cliente_geracao"),
	url(r'^financeiro/$', views.cliente_financeiro, name="cliente_financeiro"),
	url(r'^informacoes/$', views.cliente_informacoes_pessoais, name="cliente_informacoes"),
    url(r'^informacoes/pessoais/$', views.cliente_informacoes_pessoais, name="cliente_informacoes_pessoais"),
    url(r'^informacoes/usuario/$', views.cliente_informacoes_usuario, name="cliente_informacoes_usuario"),
    url(r'^informacoes/password/$', views.cliente_informacoes_password, name="cliente_informacoes_password"),
]
