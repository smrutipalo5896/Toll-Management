# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_auto_20180321_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tolllocations',
            name='place',
            field=models.CharField(max_length=250),
        ),
    ]
