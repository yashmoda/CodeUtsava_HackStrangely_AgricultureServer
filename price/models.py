# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CropPriceData(models.Model):
    crop = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return str(self.crop)