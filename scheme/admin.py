# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from scheme.models import SchemeData


class SchemeDataAdmin(admin.ModelAdmin):
    list_display = ['scheme', 'ministry', 'objective']
    search_fields = ['scheme', 'ministry']


admin.site.register(SchemeData, SchemeDataAdmin)