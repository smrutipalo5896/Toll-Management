# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-07 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
