# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170407_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordinazione',
            name='quantita',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
