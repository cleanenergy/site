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
from fatura import views

urlpatterns = [
<<<<<<< HEAD
	url(r'^pagar/$', views.fatura_pagar, name="fatura_pagar"),
	url(r'^cancelar/$', views.fatura_cancelar, name="fatura_cancelar"),
	url(r'^sucesso/$', views.fatura_sucesso, name="fatura_sucesso"),
    url(r'^processar/$', views.fatura_processar, name="fatura_processar"),
=======
	url(r'^sucesso/ass(?P<assinaturaId>[0-9]+)/$', views.fatura_sucesso, name="fatura_sucesso"),
    url(r'^pagar/ass(?P<assinaturaId>[0-9]+)/$', views.fatura_pagar, name="fatura_pagar"),
>>>>>>> c359329461fb3c40db454b2cc66cf5873bbbfceb
]