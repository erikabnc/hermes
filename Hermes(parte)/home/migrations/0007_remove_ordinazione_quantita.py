# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170411_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordinazione',
            name='quantita',
        ),
    ]
