# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-13 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180413_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='f',
            new_name='first',
        ),
    ]
