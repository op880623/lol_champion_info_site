# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0002_champion_attackspeedmax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champion',
            name='attackspeed',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='attackspeedmax',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='attackspeedperlevel',
        ),
    ]
