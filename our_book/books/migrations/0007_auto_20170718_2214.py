# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170718_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishbook',
            options={'ordering': ['-created_at']},
        ),
    ]