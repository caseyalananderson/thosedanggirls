# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelpost',
            name='post_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]