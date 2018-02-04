# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from price.models import CropPriceData


class CropPriceDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'crop', 'price']
    search_fields = ['crop']


admin.site.register(CropPriceData, CropPriceDataAdmin)
