# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20161118_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]