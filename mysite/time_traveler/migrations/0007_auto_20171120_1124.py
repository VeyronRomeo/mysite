# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_traveler', '0006_auto_20171119_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uname',
            field=models.CharField(db_index=True, max_length=12),
        ),
    ]