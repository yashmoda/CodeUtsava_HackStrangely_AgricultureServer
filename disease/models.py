# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DiseaseData(models.Model):
    disease_name_english = models.TextField()
    disease_name_hindi = models.TextField()
    symptoms_english = models.TextField()
    symptoms_hindi = models.TextField()
    prevention_english = models.TextField()
    prevention_hindi = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return str(self.disease_name_english)