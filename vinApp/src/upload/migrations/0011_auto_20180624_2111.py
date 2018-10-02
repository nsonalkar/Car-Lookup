# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-24 21:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import upload.models
import upload.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0010_remove_upload_amcool'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upload',
            name='user',
            field=models.ForeignKey(default='neil', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to=upload.models.upload_csv_file, validators=[upload.validators.csv_file_validator]),
        ),
    ]
