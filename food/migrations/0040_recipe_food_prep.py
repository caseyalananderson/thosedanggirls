# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0039_auto_20180305_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='food_prep',
            field=models.BooleanField(default=False),
        ),
    ]
