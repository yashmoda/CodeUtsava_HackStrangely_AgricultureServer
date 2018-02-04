# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ProductTypeData(models.Model):
    product_type_eng = models.CharField(max_length=20, blank=True, null=True)
    product_type_hi = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField()
    # description = models.TextField()

    def __unicode__(self):
        return str(self.product_type_eng)


AVAILABILITY = {(1, 'Available'),
                (2, 'Not Available')}


class ProductData(models.Model):
    product_type = models.ForeignKey(ProductTypeData)
    name_eng = models.TextField()
    name_hindi = models.TextField()
    price = models.IntegerField()
    key_features_english = models.TextField(blank=True, null=True)
    key_features_hindi = models.TextField(blank=True, null=True)
    description_english = models.TextField(blank=True, null=True)
    description_hindi = models.TextField(blank=True, null=True)
    # availability = models.IntegerField(choices=AVAILABILITY)
    image = models.ImageField()

    def __unicode__(self):
        return str(self.name_eng)


class ProductImage(models.Model):
    product = models.ForeignKey(ProductData)
    image = models.ImageField()

    def __unicode__(self):
        return str(self.product.name_eng)
