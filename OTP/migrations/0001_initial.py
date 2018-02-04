# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.UserData')),
            ],
        ),
    ]