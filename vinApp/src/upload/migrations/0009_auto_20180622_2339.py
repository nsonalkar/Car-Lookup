# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-22 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20180622_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='title',
        ),
        migrations.AddField(
            model_name='upload',
            name='amCool',
            field=models.BooleanField(default=True),
        ),
    ]