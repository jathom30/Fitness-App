# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 17:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0010_auto_20171010_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='rep_number',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='set_number',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='weight',
        ),
    ]
