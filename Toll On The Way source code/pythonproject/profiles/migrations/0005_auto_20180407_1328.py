# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-07 07:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180407_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='first',
            new_name='post',
        ),
    ]
