# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Products.models import ProductData
from Register.models import UserData


# class CartData(models.Model):
#     user = models.ForeignKey(UserData)
#     product = models.ForeignKey(ProductData)
#     quantity = models.CharField()
#     amount = models.CharField()
#
#     def __str__(self):
#         return str(self.user.mobile)