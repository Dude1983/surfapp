# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20160416_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]