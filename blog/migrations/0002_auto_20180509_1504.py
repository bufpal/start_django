# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 06:04
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='"longtitude,latitude" type', max_length=30, validators=[blog.models.lnglat_validator]),
        ),
    ]