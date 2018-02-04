# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Register.models import UserData


class FeedbackData(models.Model):
    user = models.ForeignKey(UserData)
    subject = models.CharField(max_length=150)
    query = models.TextField()


class ComplaintData(models.Model):
    user = models.ForeignKey(UserData)
    subject = models.CharField(max_length=255)
    query = models.TextField()
    ticket_number = models.CharField(max_length=8)