# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0002_auto_20170423_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcheck',
            name='t_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='healthcheck',
            name='z_balance',
            field=models.FloatField(default=0),
        ),
    ]