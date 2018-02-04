# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from disease.models import DiseaseData


class DiseaseDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'disease_name_english', 'disease_name_hindi']
    search_fields = ['id']


admin.site.register(DiseaseData, DiseaseDataAdmin)