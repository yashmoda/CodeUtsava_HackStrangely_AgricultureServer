# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Discussion.models import QuestionData, AnswerData


class QuestionDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'question']
    search_fields = ['user', 'question']
    
    
admin.site.register(QuestionData, QuestionDataAdmin)


class AnswerDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'answer']
    search_fields = ['user', 'question', 'answer']
    
    
admin.site.register(AnswerData, AnswerDataAdmin)