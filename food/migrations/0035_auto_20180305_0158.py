# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 01:58
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import food.models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0034_auto_20180305_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=food.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='foodprep',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
