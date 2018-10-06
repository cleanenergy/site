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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clean import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^admin/login/$', auth_views.login, {'template_name': 'accounts/login_admin.html'}, name="admin_login"),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^admin/logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='admin_logout'),
    url(r'^pagamentos/', include('fatura.urls')),
    url(r'^medicao/', include('medicao.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^password/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
]
