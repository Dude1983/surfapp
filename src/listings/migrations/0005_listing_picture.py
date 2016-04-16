# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20160416_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images/%Y-%m-%d/', verbose_name='Listing picture'),
        ),
    ]
