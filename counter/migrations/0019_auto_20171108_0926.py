# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0018_auto_20171108_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workouts',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='counter.Workout'),
            preserve_default=False,
        ),
    ]