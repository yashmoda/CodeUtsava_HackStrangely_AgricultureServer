# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class SchemeData(models.Model):
    scheme = models.TextField()
    ministry = models.TextField()
    objective = models.TextField()

    def __unicode__(self):
        return str(self.scheme)
