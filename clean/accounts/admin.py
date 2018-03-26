# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
