# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Location'),
        ),
    ]
