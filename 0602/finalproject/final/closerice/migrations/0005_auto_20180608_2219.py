# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closerice', '0004_auto_20180608_2215'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='district',
        ),
    ]
