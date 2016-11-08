# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import churchill.utils


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=churchill.utils.preview_name, verbose_name='Preview Image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=churchill.utils.thumb_name, verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=churchill.utils.image_name, verbose_name='Image'),
        ),
    ]
