# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    password = models.TextField()

    def __unicode__(self):
        return str(self.mobile)


class AddressData(models.Model):
    user = models.ForeignKey(UserData)
    name_english = models.CharField(max_length=240, blank=True, null=True)
    name_hindi = models.TextField(blank=True, null=True)
    house_number = models.CharField(max_length=240, blank=True, null=True)
    locality_english = models.CharField(max_length=240, blank=True, null=True)
    locality_hindi = models.TextField(blank=True, null=True)
    area_english = models.CharField(max_length=240, blank=True, null=True)
    area_hindi = models.TextField(blank=True, null=True)
    city_english = models.CharField(max_length=50, blank=True, null=True)
    city_hindi = models.TextField(blank=True, null=True)
    state_english = models.TextField(blank=True, null=True)
    state_hindi = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return str(self.user.mobile)
