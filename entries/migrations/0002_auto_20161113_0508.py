# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 05:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='entries.Project'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_entries', to=settings.AUTH_USER_MODEL),
        ),
    ]