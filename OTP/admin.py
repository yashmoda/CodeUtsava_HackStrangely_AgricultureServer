# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from OTP.models import OTPData


class OTPDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp']
    search_fields = ['user', 'otp']


admin.site.register(OTPData, OTPDataAdmin)
