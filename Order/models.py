# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Products.models import ProductData
from Register.models import AddressData, UserData


class OrderData(models.Model):
    user = models.ForeignKey(UserData)
    address = models.ForeignKey(AddressData)
    product = models.ForeignKey(ProductData)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    order_id = models.IntegerField()

    def __str__(self):
        return str(self.user.mobile)