# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdata',
            old_name='name',
            new_name='name_eng',
        ),
        migrations.RenameField(
            model_name='productdata',
            old_name='description',
            new_name='name_hindi',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='productdata',
            name='key_features',
        ),
        migrations.RemoveField(
            model_name='producttypedata',
            name='product_type',
        ),
        migrations.AddField(
            model_name='productdata',
            name='description_english',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='description_hindi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='key_features_english',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='key_features_hindi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producttypedata',
            name='product_type_eng',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='producttypedata',
            name='product_type_hi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]