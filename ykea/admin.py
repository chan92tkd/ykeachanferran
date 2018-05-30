# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Item
from .models import Client

# Register your models here.
admin.site.register(Item)
admin.site.register(Client)

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'clients'

class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
