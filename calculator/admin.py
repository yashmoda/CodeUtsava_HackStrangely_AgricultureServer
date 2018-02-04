# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from calculator.models import CropSpacingData, CropArrangementData


class CropSpacingDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'crop', 'spacing']
    search_fields = ['id', 'crop']


admin.site.register(CropSpacingData, CropSpacingDataAdmin)


class CropArrangementDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'crop_spacing', 'bed_size', 'bed_lines', 'seeds']
    search_fields = ['id', 'user']


admin.site.register(CropArrangementData, CropArrangementDataAdmin)
