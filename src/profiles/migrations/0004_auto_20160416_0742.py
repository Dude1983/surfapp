# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_surf_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=200, null=True, verbose_name='Location'),
        ),
    ]
