# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Feedback.models import FeedbackData, ComplaintData


class FeedbackDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'query']
    search_fields = ['user', 'subject', 'query']
    
    
admin.site.register(FeedbackData, FeedbackDataAdmin)


class ComplaintDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'query', 'ticket_number']
    search_fields = ['user', 'ticket_number']


admin.site.register(ComplaintData, ComplaintDataAdmin)
