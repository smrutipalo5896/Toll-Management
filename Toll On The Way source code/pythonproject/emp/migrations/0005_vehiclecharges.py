# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_auto_20180321_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='VEHICLECHARGES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicletype', models.CharField(max_length=250)),
                ('onewaycharge', models.CharField(max_length=250)),
                ('twowaycharges', models.CharField(max_length=250)),
            ],
        ),
    ]
