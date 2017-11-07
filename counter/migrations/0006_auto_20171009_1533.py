# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0005_auto_20171003_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='muscule_group',
            field=models.CharField(choices=[('ch', 'Chest'), ('ar', 'Arms'), ('le', 'Legs'), ('ba', 'Back'), ('co', 'Core')], max_length=2),
        ),
    ]