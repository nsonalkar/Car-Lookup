# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-22 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20180622_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='amCool',
        ),
    ]