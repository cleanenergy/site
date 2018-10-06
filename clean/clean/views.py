# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import hashlib

def home(request):
	return render(request, "clean/base.html")


