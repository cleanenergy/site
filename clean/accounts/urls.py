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
from accounts import views

urlpatterns = [
	url(r'^reset/confirm/$', views.password_reset_confirm, name="accounts_password_reset_confirm"),
	url(r'^reset/confirm/admin$', views.password_reset_confirm_admin, name="accounts_password_reset_confirm_admin"),
    url(r'^reset/(?P<token>[\w-]+)', views.password_reset, name="accounts_password_reset"),
]
