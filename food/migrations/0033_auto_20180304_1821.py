# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0032_foodpost_cover_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodpost',
            old_name='desert',
            new_name='dessert',
        ),
    ]