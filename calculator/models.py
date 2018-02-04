# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Register.models import UserData


class CropSpacingData(models.Model):
    crop = models.CharField(max_length=20)
    spacing = models.IntegerField()

    def __str__(self):
        return str(self.crop)


class CropArrangementData(models.Model):
    user = models.ForeignKey(UserData)
    crop_spacing = models.ForeignKey(CropSpacingData)
    bed_size = models.CharField(max_length=255)
    bed_lines = models.CharField(max_length=255)
    seeds = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user.mobile)
