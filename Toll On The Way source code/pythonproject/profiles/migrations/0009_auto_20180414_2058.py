# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-14 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20180414_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='first',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='last',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='vehicleno',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='vehicletype',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
