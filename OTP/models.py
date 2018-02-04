# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Register.models import UserData


class OTPData(models.Model):
    user = models.ForeignKey(UserData)
    otp = models.IntegerField()

    def __unicode__(self):
        return str(self.user.name)