# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_auto_20180308_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnesspost',
            name='post_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
