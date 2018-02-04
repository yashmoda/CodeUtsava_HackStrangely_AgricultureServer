# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Register.models import UserData, AddressData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email']
    search_fields = ['name', 'mobile', 'email']
    
    
admin.site.register(UserData, UserDataAdmin)


class AddressDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']
    search_fields = ['user', 'id']
    
    
admin.site.register(AddressData, AddressDataAdmin)
