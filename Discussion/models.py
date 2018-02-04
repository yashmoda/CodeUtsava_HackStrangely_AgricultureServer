# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Register.models import UserData


class QuestionData(models.Model):
    user = models.ForeignKey(UserData)
    question = models.TextField()

    def __unicode__(self):
        return str(self.question)


class AnswerData(models.Model):
    user = models.ForeignKey(UserData)
    question = models.ForeignKey(QuestionData)
    answer = models.TextField()