# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0026_foodpost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodpost',
            name='slug',
        ),
    ]